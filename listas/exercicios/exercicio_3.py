def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    print(convidados)


convidados = ["Manoel", "Gasque"]
novos_convidados = ["Eduardo", "Murilo", "Kael"]

adicionar_convidados(convidados, novos_convidados)