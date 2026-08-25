def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:
        quantidade = valor // nota
        valor = valor % nota

        if quantidade > 0:
            print(f"{quantidade} nota(s) de R$ {nota}")


valor = int(input("Digite o valor do saque: "))

caixa_eletronico(valor)