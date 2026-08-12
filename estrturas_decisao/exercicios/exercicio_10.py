def calcular_desconto():
    valor = float(input("Digite o valor da compra: "))

    if valor <= 100:
        desconto = 0
    elif valor <= 500:
        desconto = valor * 0.10
    else:
        desconto = valor * 0.15

    valor_final = valor - desconto

    print(f"Desconto: R$ {desconto}")
    print(f"Valor final: R$ {valor_final}")


calcular_desconto()