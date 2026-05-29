import unittest

def somar(a, b):
    return a + b

class TesteSoma(unittest.TestCase):
    def test_soma_numeros_positivos(self):
        self.assertEqual(somar(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
