from django.test import TestCase
from .models import Produto

class ProdutoTestCase(TestCase):
    def setUp(self):
        Produto.objects.create(nome="Teclado", descricao="Mecanico", preco=150.00, quantidade=10)

    def test_criacao_produto(self):
        produto = Produto.objects.get(nome="Teclado")
        self.assertEqual(produto.quantidade, 10)
