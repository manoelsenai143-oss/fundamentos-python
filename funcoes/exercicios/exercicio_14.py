def consumo_combustivel():
    distancia_percorrida = float(input(f'qual a distancia percorrida em km?'))
    quantidade_combustivel = float(input(f'qual a quantidade combustivel em litros?'))
    consumo_medio = distancia_percorrida / quantidade_combustivel
    return consumo_medio


media = consumo_combustivel()
print(f'o consumo medio é de {media} litros por km ')