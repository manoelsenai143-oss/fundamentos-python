def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    print(alunos)


alunos = ["Manoel", "Gasque", "Eduardo"]

nome = input("Digite o nome do aluno: ")
posicao = int(input("Digite a posição: "))

inserir_aluno(alunos, nome, posicao)