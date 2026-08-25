def contar_pares():
    quantidade = 0

    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            quantidade = quantidade + 1

    print(f"Quantidade de números pares: {quantidade}")


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

contar_pares()