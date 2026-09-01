def criar_ranking(pontuacoes):
    ranking = sorted(pontuacoes, reverse=True)

    return ranking


pontuacoes = [150, 300, 250, 100, 400]

ranking = criar_ranking(pontuacoes)

print(f"Ranking: {ranking}")