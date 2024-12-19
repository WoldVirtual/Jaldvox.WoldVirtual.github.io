import unittest
from src.modulo3 import Modulo3

class TestModulo3(unittest.TestCase):

    def setUp(self):
        self.modulo = Modulo3()

    def test_funcionX(self):
        resultado = self.modulo.funcionX()
        self.assertEqual(resultado, "resultado esperado de funcionX")

    def test_funcionY(self):
        resultado = self.modulo.funcionY()
        self.assertEqual(resultado, "resultado esperado de funcionY")

if __name__ == '__main__':
    unittest.main()