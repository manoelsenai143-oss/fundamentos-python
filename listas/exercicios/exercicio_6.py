def encontrar_produto(produtos, produto):
    posicao = produtos.index(produto)
    return posicao


produtos = ["Mouse", "Teclado", "Monitor"]

produto = input("Digite o produto: ")

resultado = encontrar_produto(produtos, produto)

print(f"O produto está na posição {resultado}")