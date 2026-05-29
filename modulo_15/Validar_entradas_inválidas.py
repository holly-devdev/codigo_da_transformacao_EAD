import unittest

class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Nao eh possivel dividir por zero")
        return a / b

class TesteCalculadoraErro(unittest.TestCase):
    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ZeroDivisionError):
            calc.dividir(10, 0)

if __name__ == "__main__":
    unittest.main()
