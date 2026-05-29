usuario_correto = "admin"
senha_correta = "1234"
tentativas = 3

while tentativas > 0:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        tentativas -= 1
        print("Credenciais inválidas! Tentativas restantes:", tentativas)

if tentativas == 0:
    print("Acesso bloqueado! Você excedeu o limite de tentativas.")
