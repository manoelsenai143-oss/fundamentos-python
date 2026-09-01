def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)
    soma = sum(temperaturas)
    media = soma / quantidade
    ordenadas = sorted(temperaturas)

    return quantidade, soma, media, ordenadas


temperaturas = [25, 30, 18, 22, 28]

quantidade, soma, media, ordenadas = analisar_temperaturas(temperaturas)

print(f"Quantidade de temperaturas: {quantidade}")
print(f"Soma das temperaturas: {soma}")
print(f"Média: {media}")
print(f"Temperaturas ordenadas: {ordenadas}")