def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)


nomes = ["Manoel", "Gasque"]

nome = input("Digite um nome: ")

adicionar_nome(nomes, nome)