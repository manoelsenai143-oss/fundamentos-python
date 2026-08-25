def somar_pares():
    soma = 0

    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            soma = soma + i

    print(f"A soma dos números pares é: {soma}")


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

somar_pares()