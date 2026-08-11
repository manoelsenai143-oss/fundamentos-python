def imc():
    peso = float(input('Qual o seu peso?'))
    altura = float(input('Qual a sua altura?'))
    imc = peso / (altura ** 2)
    return imc

imc = imc()
print(f'o seu imc é: {imc}')