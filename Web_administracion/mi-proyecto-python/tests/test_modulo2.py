import unittest
from src.modulo2 import Modulo2

class TestModulo2(unittest.TestCase):

    def setUp(self):
        self.modulo = Modulo2()

    def test_funcionA(self):
        resultado = self.modulo.funcionA()
        self.assertEqual(resultado, "resultado esperado A")  # Reemplaza con el resultado esperado

    def test_funcionB(self):
        resultado = self.modulo.funcionB()
        self.assertEqual(resultado, "resultado esperado B")  # Reemplaza con el resultado esperado

if __name__ == '__main__':
    unittest.main()