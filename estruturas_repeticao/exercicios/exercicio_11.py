def fatorial():
    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i

    print(f"O fatorial de {numero} é: {resultado}")


numero = int(input("Digite um número: "))

fatorial()