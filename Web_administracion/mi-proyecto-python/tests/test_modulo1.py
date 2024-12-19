import unittest
from src.modulo1 import Modulo1

class TestModulo1(unittest.TestCase):

    def setUp(self):
        self.modulo = Modulo1()

    def test_funcion1(self):
        resultado = self.modulo.funcion1()
        self.assertEqual(resultado, "resultado esperado de funcion1")

    def test_funcion2(self):
        resultado = self.modulo.funcion2()
        self.assertEqual(resultado, "resultado esperado de funcion2")

if __name__ == '__main__':
    unittest.main()