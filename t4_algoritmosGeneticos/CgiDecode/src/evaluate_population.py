from src.get_fitness_cgi_decode import get_fitness_cgi_decode
from src.evaluate_condition import clear_maps
def evaluate_population(population):
    fitness = {}
    for member in population:
        fitness[member] = get_fitness_cgi_decode(member)
        clear_maps()
    return fitness
