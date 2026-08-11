def valor_prestacao():
    valor_produto = float(input('Digite o valor do produto: '))
    quantidade_parcelas = int(input('Digite a quantidade de parcelas: '))
    valor_parcela = valor_produto / quantidade_parcelas
    return valor_parcela

valor_final_parcelas = valor_prestacao()
print(f'o valor de cada parcela é {valor_final_parcelas}')