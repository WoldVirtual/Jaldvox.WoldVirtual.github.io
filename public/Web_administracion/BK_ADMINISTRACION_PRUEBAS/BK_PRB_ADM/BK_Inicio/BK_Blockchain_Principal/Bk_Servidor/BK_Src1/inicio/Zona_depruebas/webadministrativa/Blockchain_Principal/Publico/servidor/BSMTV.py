from flask import Flask
from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.BSnts import obtener_blockchain, agregar_bloque, obtener_bloque
from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.Bksvbsd import registrar_usuario, verificar_credenciales
from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.Bksvmain import manejar_accion
from Metaverso_Crypto.webadministrativa.Blockchain_Principal.Publico.servidor.Bksvutills import configurar_rutas

app = Flask(__name__)
configurar_rutas(app)

if __name__ == '__main__':
    # Ejemplo de registro de usuario
    registrar_usuario("usuario1", "contrasena_segura")

    # Ejemplo de verificación de credenciales y manejo de entorno virtual
    usuario_actual = "usuario1"
    contrasena_ingresada = "contrasena_segura"

    if verificar_credenciales(usuario_actual, contrasena_ingresada):
        print("Inicio de sesión exitoso")
        accion_usuario = "explorar"
        manejar_accion(usuario_actual, accion_usuario)
    else:
        print("Credenciales incorrectas")

    app.run(debug=True)
