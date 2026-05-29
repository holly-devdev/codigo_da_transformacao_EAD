class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, bateria):
        super().__init__(marca, modelo)
        self.bateria = bateria

    def exibir_info(self):
        print("Carro Elétrico:", self.marca, self.modelo, "- Bateria:", self.bateria, "km")


carro_nasa = CarroEletrico("Tesla", "Model 3", 400)
carro_nasa.exibir_info()
