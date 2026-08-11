def cadastro():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    profissao = input("Digite seu profissao: ")
    cidade = input("Digite sua cidade: ")
    return nome, idade, profissao, cidade

nome, idade, profissao, cidade = cadastro()
print(f"===== CADASTRO DE UMA PESSOA =====\n"
      f"\n"
      f"NOME: {nome}\n"
      f"IDADE: {idade}\n"
      f"PROFISSAO: {profissao}\n"
      f"CIDADE: {cidade}\n"
      f"\n"
      f"==================================")