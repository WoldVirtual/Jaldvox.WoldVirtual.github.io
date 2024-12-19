# Mi Proyecto Python

Este proyecto es un conjunto de módulos de Python que incluye un módulo principal llamado `BotonDeEncendido`, el cual activa todo el sistema. A continuación se detallan los componentes del proyecto.

## Estructura del Proyecto

```
mi-proyecto-python
├── src
│   ├── __init__.py
│   ├── boton_de_encendido.py
│   ├── modulo1.py
│   ├── modulo2.py
│   └── modulo3.py
├── tests
│   ├── __init__.py
│   ├── test_boton_de_encendido.py
│   ├── test_modulo1.py
│   ├── test_modulo2.py
│   └── test_modulo3.py
├── requirements.txt
└── README.md
```

## Instalación

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

```
pip install -r requirements.txt
```

## Uso

Para activar el sistema, importa la clase `BotonDeEncendido` desde el módulo `boton_de_encendido` y llama al método `activar_sistema`.

```python
from src.boton_de_encendido import BotonDeEncendido

boton = BotonDeEncendido()
boton.activar_sistema()
```

## Pruebas

Las pruebas unitarias están ubicadas en el directorio `tests`. Para ejecutar las pruebas, utiliza el siguiente comando:

```
pytest tests/
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.