"""
Este archivo contiene la lógica relacionada con la blockchain. Aquí se pueden definir funciones y clases que manejen la interacción con la blockchain.
"""

from web3 import Web3
import datetime
import time
import requests
import json
from threading import Thread
from flask_cors import CORS
from eth_account import Account
from flask_sockets import Sockets
from flask_mysqldb import MySQL
import jwt
from functools import wraps

# Aquí puedes agregar funciones y clases relacionadas con la blockchain.