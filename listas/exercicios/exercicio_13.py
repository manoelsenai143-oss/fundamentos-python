def adicionar_cliente(fila, cliente):
    fila.append(cliente)


def atender_cliente(fila):
    cliente_atendido = fila.pop(0)

    return cliente_atendido


fila = []

while True:
    cliente = input("Digite o nome do cliente (ou 'sair' para finalizar): ")

    if cliente.lower() == "sair":
        break

    adicionar_cliente(fila, cliente)


print(f"\nFila atual: {fila}")

if len(fila) > 0:
    atendido = atender_cliente(fila)

    print(f"Cliente atendido: {atendido}")
    print(f"Fila atualizada: {fila}")
else:
    print("Não há clientes na fila.")