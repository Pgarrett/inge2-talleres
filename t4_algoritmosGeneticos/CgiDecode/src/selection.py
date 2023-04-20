import random


def selection(evaluated_population, tournament_size):
    populationKeys = list(evaluated_population.keys())
    participants = random.choices(populationKeys, None, k=tournament_size)
    winner = participants[0]
    for p in participants:
        if evaluated_population[p] < evaluated_population[winner]:
            winner = p
    return winner, evaluated_population[winner]
