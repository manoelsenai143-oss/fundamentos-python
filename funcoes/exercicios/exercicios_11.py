def horas_trabalho():
    horas= float(input(f"Digite a quantidade que você recebe por hora: "))
    quantidade_horas = float(input(f"Quantas horas você trabalha diariamente :"))
    calcular_dia = horas * quantidade_horas
    return calcular_dia

salario= horas_trabalho()
print(f"O seu salario diario é {salario}")