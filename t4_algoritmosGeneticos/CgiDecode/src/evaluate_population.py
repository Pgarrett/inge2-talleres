from src.get_fitness_cgi_decode import get_fitness_cgi_decode
from src.evaluate_condition import clear_maps
def evaluate_population(population):
    fitness = {}
    for i in range(0, len(population)):
        fitness[i] = get_fitness_cgi_decode(population[i])
        clear_maps()
    return fitness
