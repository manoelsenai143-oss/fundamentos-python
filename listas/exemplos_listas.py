def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é {nome}")

lista_de_nomes = ["Renan", "Moises", "Rafael", "Ana", "Clayton"]
mostrar_nomes(lista_de_nomes)

# Adicionando novo nome na lista
def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nome(lista_de_nomes, "Manoel")

# Adicionando novo nome em uma posição específica
def adicionar_nome_posição(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao} da lísta:{nomes}")

adicionar_nome_posição(lista_de_nomes, "Rogério", 2)

# Jnutando duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes}  foram inseridos na lista {nomes}")

novos_nomes = ["Francisco", "Márcio"]

juntar_nomes(lista_de_nomes, novos_nomes)

# Removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido da lista {nomes}")

remover_nome_pelo_valor(lista_de_nomes, "Márcio")

# Removendo nome pelo indice
def remover_anome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f"O nome da posição {posicao} é {nomes[posicao]}, foi removido!")

remover_anome_pelo_indice(lista_de_nomes, 4)

# Descobrindo a posição (index) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        posicao = nomes.index(nome)
        print(f"A posição do nome {nome} é {posicao}")

encontrar_posicao_pelo_valor(lista_de_nomes, "Moises")

# contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"Quantidade de nomes da lista e: {quantidade}")

quantidade_de_nomes(lista_de_nomes)

# ordenando os elementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(lista_de_nomes)
    print(f"a lista ordenada: {lista_de_nomes_ordenados}")

ordenar_nomes(lista_de_nomes)

#operacoes matematicas
#calcular media
def calcular_media(notas):
    total= sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"a media das notas: {media} ")

notas_semestre = [7.8, 6.5, 9, 8.7, 9.5]
calcular_media(notas_semestre)


def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return ordenadas, media

notas_ordenadas, media = gerenciar_notas(notas_semestre, 3.5 )
print(f"notas ordenadas = {notas_ordenadas}")
print(f"medias das notass = {media}")

#lista de listas

def adidiconar_produto(produtos, produto):
    produtos.append(produto)
    print(f"minha lista de produtos: {produtos[0][2]}")

lista_produtos = [
    ["Arroz", 2, 32.00],
    ["feijão",3, 8.50]
]
novo_produto = ["Café", 2, 28.00]

adidiconar_produto(lista_produtos, novo_produto)


def quantidade_total_produtos(produtos):
    quantidades = []

    for produto in produtos:
        print(f'rodando laço for em lista_produtos: {produto[1]}')
        quantidades.append(produto[1])

    return sum(quantidades)

quantidade_produtos = quantidade_total_produtos(lista_produtos)
print(f'quantidade de produtos: {quantidade_produtos}')


def valor_total_produtos(produtos):
    valores = []
    for produto in produtos:
        valores.append(produto[2] * produto[1])

    return sum(valores)

precor_total_produtos = valor_total_produtos(lista_produtos)
print(f'precor total: {precor_total_produtos}')
  