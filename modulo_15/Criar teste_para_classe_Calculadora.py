import unittest

class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        return a / b

class TesteCalculadora(unittest.TestCase):
    def test_somar(self):
        calc = Calculadora()
        self.assertEqual(calc.somar(10, 5), 15)

    def test_dividir(self):
        calc = Calculadora()
        self.assertEqual(calc.dividir(10, 2), 5)

if __name__ == "__main__":
    unittest.main()
