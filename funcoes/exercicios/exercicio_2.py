from variaveis.variaveis import idade


def nome_idade():
    nome = input('Qual o seu nome?')
    idade= int(input('Qual a sua idade?'))
    print(f"{nome} tem {idade} anos")

nome_idade()

