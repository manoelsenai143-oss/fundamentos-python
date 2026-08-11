def preco_desconto():
    preco = float(input(f'qual o preco do produto?'))
    desconto = float(input(f'qual a desconto do produto?'))
    calculo_desconto = preco * desconto / 100
    calculado = preco - calculo_desconto


    return calculado
total_desconto = preco_desconto()
print(f'o preço com desconto ficou em {total_desconto}')