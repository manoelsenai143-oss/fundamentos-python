def validar_senha(senha_correta):
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == senha_correta:
            print("Acesso permitido!")
            break
        else:
            print("Senha incorreta!")
            tentativas = tentativas + 1

    if tentativas == 3:
        print("Acesso bloqueado!")


validar_senha("1234")