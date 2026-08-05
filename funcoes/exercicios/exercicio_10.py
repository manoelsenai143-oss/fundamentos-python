def conversao_temperatura():
    temperatura_celcius = float(input('informe a temperatura: '))
    conversao_fahrenheit = temperatura_celcius * 1.8 + 32
    return conversao_fahrenheit

convertido = conversao_temperatura()
print(f'a conversao final é {convertido}')