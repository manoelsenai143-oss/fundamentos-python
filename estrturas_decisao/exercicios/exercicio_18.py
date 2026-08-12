def calcular_frete():
    valor = float(input("Digite o valor da compra: "))

    if valor <= 100:
        frete = 20
    elif valor <= 300:
        frete = 10
    else:
        frete = 0

    total = valor + frete

    print(f"Frete: R$ {frete}")
    print(f"Valor total: R$ {total}")


calcular_frete()