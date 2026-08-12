def preco_ingresso():
    idade = int(input("Digite a idade: "))

    if idade <= 5:
        print("Ingresso gratuito")
    elif idade <= 12:
        print("Preço: R$ 10,00")
    elif idade <= 59:
        print("Preço: R$ 20,00")
    else:
        print("Preço: R$ 10,00")


preco_ingresso()