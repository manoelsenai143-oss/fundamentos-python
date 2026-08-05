def conversao():
    valor_metro = float(input('digite o valor do metro: '))
    conversao_centimetro = valor_metro*100
    return conversao_centimetro


conversao_centimetro = conversao()
print(f'o valor em centimetros é{conversao_centimetro}')

