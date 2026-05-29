try:
    idade = int(input("Digite a sua idade: "))
    if idade < 0:
        raise ValueError("Erro: A idade não pode ser um número negativo!")
    print("Idade cadastrada com sucesso:", idade)
except ValueError as erro:
    print(erro)
