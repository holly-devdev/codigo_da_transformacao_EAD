class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print("Carro:", self.marca, self.modelo)

# Teste
meu_carro = Carro("Ford", "Fiesta")
meu_carro.exibir_info()
