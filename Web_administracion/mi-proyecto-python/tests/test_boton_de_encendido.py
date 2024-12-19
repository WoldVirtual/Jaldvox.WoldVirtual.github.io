import unittest
from src.boton_de_encendido import BotonDeEncendido

class TestBotonDeEncendido(unittest.TestCase):

    def setUp(self):
        self.boton = BotonDeEncendido()

    def test_activar_sistema(self):
        resultado = self.boton.activar_sistema()
        self.assertTrue(resultado, "El sistema no se activó correctamente.")

if __name__ == '__main__':
    unittest.main()