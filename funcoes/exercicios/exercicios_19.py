def comsumo_energia():
    consumo_kwh = float(input('Digite o valor consumido em kwh: '))
    preco_kwh = float(input('digite o preço do kwh: '))
    valor_total = consumo_kwh * preco_kwh
    return valor_total

total = comsumo_energia()
print(f'{total}')
