def remover_produto(produtos, produto):
    produtos.remove(produto)
    print(produtos)


produtos = ["Mouse", "Teclado", "Monitor"]

produto = input("Digite o produto para remover: ")

remover_produto(produtos, produto)