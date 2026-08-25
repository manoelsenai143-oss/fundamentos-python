def menu():
    opcao = 0

    while opcao != 4:

        print("1 - Exibir números de 1 a 10")
        print("2 - Exibir números pares")
        print("3 - Exibir tabuada")
        print("4 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            for i in range(1, 11):
                print(i)

        elif opcao == 2:
            for i in range(1, 11):
                if i % 2 == 0:
                    print(i)

        elif opcao == 3:
            numero = int(input("Digite um número: "))

            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")

        elif opcao == 4:
            print("Saindo...")

        else:
            print("Opção inválida!")


menu()