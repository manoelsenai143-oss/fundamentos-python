def calcular_media():
   nota1 = float(input('Qual a primeira nota?'))
   nota2 = float(input('Qual a segunda nota?'))
   nota3 = float(input('Qual a terceira nota?'))
   media = (nota1 + nota2 + nota3) / 3
   return media

nota_final= calcular_media()
print(f'a media final é {nota_final}')





