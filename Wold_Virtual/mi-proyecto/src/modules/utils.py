def obtener_fecha_hora_actual():
    """Devuelve la fecha y hora actual en formato legible."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validar_direccion(direccion):
    """Valida si una dirección es correcta (ejemplo para direcciones de Ethereum)."""
    if Web3.isChecksumAddress(direccion):
        return True
    return False

def generar_token_jwt(datos, clave_secreta, tiempo_expiracion=3600):
    """Genera un token JWT a partir de los datos proporcionados."""
    return jwt.encode(datos, clave_secreta, algorithm='HS256', expires_delta=datetime.timedelta(seconds=tiempo_expiracion))

def decodificar_token_jwt(token, clave_secreta):
    """Decodifica un token JWT y devuelve los datos contenidos en él."""
    try:
        return jwt.decode(token, clave_secreta, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None