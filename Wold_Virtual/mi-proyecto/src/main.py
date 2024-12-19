from flask import Flask
from flask_cors import CORS
from blockchain import Blockchain  # Asegúrate de que la clase Blockchain esté definida en blockchain.py
from modules.auth import Auth
from modules.database import Database
from modules.network import Network
from modules.utils import Utils

app = Flask(__name__)
CORS(app)

# Inicializar módulos
auth = Auth()
database = Database()
network = Network()
utils = Utils()

@app.route('/')
def index():
    return "Bienvenido a la plataforma Notas"

if __name__ == "__main__":
    app.run(debug=True)