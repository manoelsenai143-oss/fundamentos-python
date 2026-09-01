notas = [7.5, 6.0, 8.5, 9.0, 5.5]


def adicionar_nota(notas, nota):
    notas.append(nota)


def inserir_nota(notas, posicao, nota):
    notas.insert(posicao, nota)


def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)


def remover_nota(notas, nota):
    notas.remove(nota)


def remover_ultima_nota(notas):
    return notas.pop()


def encontrar_posicao(notas, nota):
    return notas.index(nota)


def quantidade_notas(notas):
    return len(notas)


def ordenar_notas(notas):
    return sorted(notas)


def notas_inversas(notas):
    return list(reversed(notas))


def soma_notas(notas):
    return sum(notas)


def media_notas(notas):
    return sum(notas) / len(notas)


print(f"Notas iniciais: {notas}")

adicionar_nota(notas, 7.0)
print(f"\nApós adicionar uma nota: {notas}")

inserir_nota(notas, 2, 10.0)

print(f"Após inserir uma nota: {notas}")
adicionar_varias_notas(notas, [8.0, 6.5])
print(f"Após adicionar várias notas: {notas}")

remover_nota(notas, 5.5)
print(f"Após remover a nota: {notas}")

ultima = remover_ultima_nota(notas)
print(f"Última nota removida: {ultima}")
print(f"Notas atuais: {notas}")

nota_procurada = 8.5

if nota_procurada in notas:
    posicao = encontrar_posicao(notas, nota_procurada)
    print(f"A nota {nota_procurada} está na posição {posicao}")

quantidade = quantidade_notas(notas)
print(f"Quantidade de notas: {quantidade}")

ordenadas = ordenar_notas(notas)
print(f"Notas ordenadas: {ordenadas}")

inversas = notas_inversas(notas)
print(f"Notas inversas: {inversas}")

soma = soma_notas(notas)
print(f"Soma das notas: {soma}")

media = media_notas(notas)
print(f"Média da turma: {media}")