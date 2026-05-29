class SaldoInsuficienteError(Exception):
    pass


class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Erro: Saldo insuficiente para realizar o saque!")
        self.saldo -= valor
        print("Saque realizado! Saldo atual:", self.saldo)


conta = ContaBancaria(500)

try:
    conta.sacar(600)
except SaldoInsuficienteError as erro:
    print(erro)
