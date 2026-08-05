def exibir_mensagem():
    print('hello world!!!!!')

def somar():
    valor_1 = 50
    valor_2 = 20
    total = valor_1 + valor_2
    print(f'A soma vale {total}')

def calcular_media():
   nota1 = float(input('Qual a primeira nota?'))
   nota2 = float(input('Qual a segunda nota?'))
   media = (nota1 + nota2) / 2
   return media


exibir_mensagem()
somar()
nota_final= calcular_media()
print(f'a nota final é {nota_final}')