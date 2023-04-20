import random


def crossover(parent1, parent2, seed=None):
    random.seed(seed)
    crossoverLimit = random.randint(1, min(len(parent1), len(parent2)))
    offspring1 = parent1[0:crossoverLimit] + parent2[crossoverLimit:len(parent2)]
    offspring2 = parent2[0:crossoverLimit] + parent1[crossoverLimit:len(parent1)]
    return offspring1, offspring2
