def classificar_velocidade():
    velocidade = float(input("Digite a velocidade do veículo: "))

    if velocidade <= 60:
        print(f"Velocidade permitida")
    elif velocidade <= 80:
        print(f"Atenção: velocidade acima do permitido")
    else:
        print(f"Multa por excesso de velocidade")


classificar_velocidade()