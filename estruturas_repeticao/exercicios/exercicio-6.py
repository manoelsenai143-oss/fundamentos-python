def somar_ate():
    soma = 0

    for i in range(1, numero + 1):
        soma = soma + i

    print(f'A soma é: {soma}')


numero = int(input("Digite um número: "))

somar_ate()