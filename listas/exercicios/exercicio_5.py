def remover_item(itens, posicao):
    removido = itens.pop(posicao)
    return removido


itens = ["Caderno", "Lápis", "Caneta"]

posicao = int(input("Digite a posição para remover: "))

resultado = remover_item(itens, posicao)

print(f"Item removido: {resultado}")
print(f"Lista atualizada: {itens}")