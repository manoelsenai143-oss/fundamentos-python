def mostrar_numero_while():
    contador = 0
    while contador < 10:
        contador += 1
        print(f'contagem atual: {contador}')


#mostrar_numero_while()


def contagem_regressiva():
    valor_contagem = int(input('digite um número maior que 10: '))
    if valor_contagem < 10:
        print('valor inválido')
    else:
        while valor_contagem >= 1:
            print(f'contagem regressiva: {valor_contagem}')
            valor_contagem -= 1
        print('decolando!!')


#ontagem_regressiva()

def soma_com_while():
    while True:
        num_1 = int(input('digite o primeiro valor: '))
        num_2 = int(input('digite o segundo valor: '))

        if num_1 == 0:
            print('função de soma encerrada!')
            break
        else:
          soma = num_1 + num_2
        print(f'o resultado da soma é {soma}')

soma_com_while()