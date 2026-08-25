def jogo_adivinhacao(numero_secreto):
    acertou = False

    while acertou == False:
        palpite = int(input("Digite seu palpite: "))

        if palpite == numero_secreto:
            print("Você acertou!")
            acertou = True

        elif palpite > numero_secreto:
            print("O número secreto é menor.")

        else:
            print("O número secreto é maior.")


jogo_adivinhacao(7)