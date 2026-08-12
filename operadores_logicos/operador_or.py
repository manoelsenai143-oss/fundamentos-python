#operador or

def posso_compra():
    TEM_CARTA0 = False
    tem_dinheiro = bool(input(f'voce tem dinheiro pra comprar? '))
    autorizado = tem_dinheiro or TEM_CARTA0
    print(f'vou comer MC-Donalds hoje? {autorizado}')

posso_compra()