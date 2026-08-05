def perimetro_retangulo():
    base = float(input('digite o valor da base: '))
    altura = float(input('digite sua altura: '))
    perimetro = 2 * (base + altura)
    return perimetro



perimetro = perimetro_retangulo()
print(f'a area do reatngulo é {perimetro}')