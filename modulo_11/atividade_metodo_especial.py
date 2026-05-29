class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return self.marca + " " + self.modelo


meu_carro = Carro("Ford", "Fiesta")
print(meu_carro)
