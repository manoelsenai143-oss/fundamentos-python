def comissao():
    salario = float(input(f'qual o seu salario?'))
    vendas = float(input(f'quanto voce arrecadou de vendas?'))
    comissao_vendas = float(input(f'quanto de porcentagem vc tira da comissão ?'))
    calculo_comissao = comissao_vendas * vendas / 100
    salario_final = salario + calculo_comissao
    return salario_final

final = comissao()
print(f'o seu salario final é {final}')
