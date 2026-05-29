opcao = 0

# O programa vai repetir tudo aqui dentro enquanto a opção não for 3
while opcao != 3:
    print("\n--- MENU ---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")
    
    opcao = int(input("Escolha uma opção (1, 2 ou 3): "))
    
    if opcao == 1:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print("Resultado da soma:", n1 + n2)
        
    elif opcao == 2:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        print("Resultado da subtração:", n1 - n2)
        
    elif opcao == 3:
        print("Saindo do programa... Até logo!")
        
    else:
        print("Opção inválida! Digite 1, 2 ou 3.")
