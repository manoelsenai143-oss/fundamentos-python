def adicionar_produtos(compras, produtos):
    compras.extend(produtos)


def cancelar_compra(compras, produto):
    compras.remove(produto)


compras = ["Arroz", "Feijão"]
produtos = ["Leite", "Pão", "Café"]

adicionar_produtos(compras, produtos)

print(f"Lista de compras: {compras}")

produto = input("Digite o produto que deseja cancelar: ")

if produto in compras:
    cancelar_compra(compras, produto)
    print(f"Lista atualizada: {compras}")
else:
    print("Produto não encontrado.")