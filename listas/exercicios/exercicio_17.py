def vender_produto(estoque, produto):

    if produto in estoque:
        estoque.remove(produto)
        print(f"{produto} foi vendido.")
    else:
        print(f"{produto} não está disponível.")

    return estoque


estoque = ["Mouse", "Teclado", "Monitor", "Webcam"]

print(f"Estoque atual: {estoque}")

produto = input("Digite o produto que deseja comprar: ")

resultado = vender_produto(estoque, produto)

print(f"Estoque atualizado: {resultado}")