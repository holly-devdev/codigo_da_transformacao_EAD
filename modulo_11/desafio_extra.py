class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


class Biblioteca:
    def __init__(self):
        self.lista_de_livros = []

    def adicionar_livro(self, livro):
        self.lista_de_livros.append(livro)

    def emprestar_livro(self, titulo_do_livro):
        for livro in self.lista_de_livros:
            if livro.titulo == titulo_do_livro:
                if livro.disponivel:
                    livro.disponivel = False
                    print("Você pegou o livro '" + titulo_do_livro + "' emprestado!")
                    return
                else:
                    print("Desculpe, o livro '" + titulo_do_livro + "' já está emprestado.")
                    return
        print("O livro '" + titulo_do_livro + "' não foi encontrado.")


biblioteca = Biblioteca()
l1 = Livro("O Alquimista", "Paulo Coelho")
biblioteca.adicionar_livro(l1)
biblioteca.emprestar_livro("O Alquimista")
