def adicionar_nota(notas, nota):
    notas.append(nota)


def remover_nota(notas, nota):
    notas.remove(nota)


def media_notas(notas):
    total = sum(notas)
    quantidade = len(notas)

    return total / quantidade


notas = [7.0, 8.5, 6.0]

nova_nota = float(input("Digite uma nova nota: "))

adicionar_nota(notas, nova_nota)

print(f"Notas: {notas}")

nota_remover = float(input("Digite a nota que deseja remover: "))

if nota_remover in notas:
    remover_nota(notas, nota_remover)

print(f"Notas atualizadas: {notas}")

media = media_notas(notas)

print(f"Média das notas: {media}")