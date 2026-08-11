def conversao_idade():
    idade_em_anos = int(input(f'qual a idade em anos ?'))
    idade_em_meses = idade_em_anos * 12
    print(f'sua idade em meses são {idade_em_meses} meses')
    idade_em_dias =  idade_em_anos * 365
    print(f'sua iadade aproximadamente em dias são {idade_em_dias} dias')


conversao_idade()


