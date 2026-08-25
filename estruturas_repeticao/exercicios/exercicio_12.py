def eh_primo():
    primo = True

    if numero < 2:
        primo = False

    for i in range(2, numero):
        if numero % i == 0:
            primo = False

    if primo:
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")


numero = int(input("Digite um número: "))

eh_primo()