def aluno_aprovado():
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))

    media = (nota_1 + nota_2) / 2

    if media >= 7:
        print('Aprovado')
    elif media >= 5 and media < 7:
        print('recuperação')
    else:
        print('Reprovado')


# aluno_aprovado()


def login():
    e_mail = 'manoel.moraes@gmail.com'
    senha = '1234'
    codigo_secreto = '#456@'

    e_mail_input = input('Digite o seu e-mail: ')
    senha_input = input('Digite sua senha: ')

    if e_mail_input == e_mail and senha_input == senha:
        print('Logado')
        acessar_admin = input('Deseja acessar o administrador? (Digite S ou N)')
        if acessar_admin == 'S':
            codigo_secreto_input = input('Digite o seu codigo secreto: ')
            if codigo_secreto_input == codigo_secreto:
                print('Logado')
            else:
                print('código errado')

    else:
        print('Senha ou usuario incorretos(as)')

login()

