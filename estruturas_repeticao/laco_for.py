def mostra_numero():
    for i in range(1, 6):
        print(f'o numero atual é {i}')



#mostrar_numero()

def mostra_numero_alterado():
    for num in range(0, 20, 2):
        print(f'o numero atual é {num}')


#mostra_numero_alterado()


def somar_numeros():
    total = 0
    for valor in range(1, 20):
        total += valor
        print(total)

#somar_numeros()


def mostrar_numeros_pares():
    for numero in range(1, 21):
        if numero % 2 == 0:
            print(f'numeros  pares {numero}' )


#mostrar_numeros_pares()



def mostrar_item_lista():
    sacola_de_frutas = ['maça', 'banana', 'pera', 'abacate']
    for fruta in sacola_de_frutas:
        print(f' na minha sacola contem {fruta}')


#mostrar_item_lista()


def laco_aninhado():
    nomes = ['Manoel', 'mug', 'gasque']
    notas = [8, 9, 10]
    for nome in nomes:
        print(f"nome do aluno {nome}")
        for nota in notas:
            print(f"nota do aluno {nota}")

laco_aninhado()