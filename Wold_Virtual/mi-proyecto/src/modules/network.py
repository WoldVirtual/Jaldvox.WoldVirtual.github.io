def send_request(url, data=None):
    if data:
        response = requests.post(url, json=data)
    else:
        response = requests.get(url)
    return response.json()

def receive_data(socket):
    while True:
        data = socket.recv()
        if data:
            process_data(data)

def process_data(data):
    # Aquí se puede agregar la lógica para procesar los datos recibidos
    print("Datos recibidos:", data)