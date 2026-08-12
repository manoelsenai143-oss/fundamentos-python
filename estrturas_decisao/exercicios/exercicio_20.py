def caixa_eletronico():
    saldo = float(input("Digite o saldo disponível: "))
    saque = float(input("Digite o valor que deseja sacar: "))

    if saque > saldo:
        print("Saldo insuficiente")
    elif saque <= 0:
        print("Valor de saque inválido")
    else:
        novo_saldo = saldo - saque
        print("Saque realizado com sucesso")
        print(f"Novo saldo: R$ {novo_saldo}")


caixa_eletronico()