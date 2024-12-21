"""
This script handles user login and blockchain operations using Flask.
"""

from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
import datetime

# Clase Blockchain refactorizada
class Blockchain:
    """
    Blockchain class to manage the chain of blocks.
    """
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain = []
        self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        """
        Create the genesis block and add it to the chain.
        """
        genesis_block = {
            'index': 0,
            'timestamp': str(datetime.datetime.now()),
            'data': 'Bloque Génesis',
            'previous_hash': '0',
            'hash': self.hash_bloque('Bloque Génesis', '0')
        }
        self.chain.append(genesis_block)

    def agregar_bloque(self, data):
        """
        Add a new block to the chain with the given data.
        """
        previous_block = self.chain[-1]
        new_block = {
            'index': len(self.chain),
            'timestamp': str(datetime.datetime.now()),
            'data': data,
            'previous_hash': previous_block['hash'],
            'hash': self.hash_bloque(data, previous_block['hash'])
        }
        self.chain.append(new_block)

    def hash_bloque(self, data, previous_hash):
        """
        Calculate the hash of a block based on its data and previous hash.
        """
        contenido = data + previous_hash + str(datetime.datetime.now())
        return hashlib.sha256(contenido.encode()).hexdigest()

    def obtener_informacion_cadena(self):
        """
        Get information about the blockchain, including its length and blocks.
        """
        informacion = {
            'longitud': len(self.chain),
            'bloques': [block for block in self.chain],
        }
        return informacion

    def validar_cadena(self):
        """
        Validate the blockchain by checking the hashes of each block.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != previous_block['hash']:
                return False
        return True

# Crear una instancia de Blockchain
blockchain = Blockchain()

# Almacenamiento en memoria para usuarios registrados (simulado)
usuarios = {}

# Configuración básica del servidor web con Flask
app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

# Ruta principal - pantalla de inicio de sesión
@app.route('/')
def login():
    """
    Render the login page.
    """
    return """
    <html>
        <head>
            <title>Iniciar sesión</title>
        </head>
        <body>
            <h1>Iniciar sesión</h1>
            <form action="/login" method="POST">
                <label for="username">Usuario:</label>
                <input type="text" id="username" name="username" required><br><br>
                <label for="password">Contraseña:</label>
                <input type="password" id="password" name="password" required><br><br>
                <button type="submit">Iniciar sesión</button>
            </form>
        </body>
    </html>
    """

# Ruta de manejo de inicio de sesión
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    # Validar si el usuario ya existe o registrarlo
    if username in usuarios:
        # Validar contraseña
        if usuarios[username] != password:
            return "Contraseña incorrecta. <a href='/'>Inténtalo de nuevo</a>"
    else:
        # Registrar al usuario
        usuarios[username] = password

    # Iniciar la sesión para el usuario
    session['username'] = username

    # Crear un hash único para esta sesión
    hash_usuario = hashlib.sha256(f'{username}{datetime.datetime.now()}'.encode()).hexdigest()

    # Agregar un nuevo bloque con los datos del usuario
    blockchain.agregar_bloque(f'Usuario {username} ha iniciado sesión con hash: {hash_usuario}')

    # Redirigir al usuario a la página principal con los datos
    return redirect(url_for('pagina_principal'))

# Ruta de página principal una vez iniciado sesión
@app.route('/pagina_principal')
def pagina_principal():
    # Validar si el usuario ha iniciado sesión
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    validacion = blockchain.validar_cadena()

    return f"""
    <html>
        <head>
            <title>Página Principal</title>
        </head>
        <body>
            <h1>Bienvenido {username}</h1>
            <p>Has iniciado sesión correctamente.</p>
            <p>La cadena de bloques es válida: {validacion}</p>
            <p>Hash del último bloque: {blockchain.chain[-1]['hash']}</p>
            <a href='/logout'>Cerrar sesión</a>
        </body>
    </html>
    """

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Iniciar la aplicación Flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
