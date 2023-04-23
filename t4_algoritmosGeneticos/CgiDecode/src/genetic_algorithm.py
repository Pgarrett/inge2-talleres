import random
from src.create_population import create_population
from src.crossover import crossover
from src.evaluate_condition import distances_true, clear_maps
from src.evaluate_population import evaluate_population
from src.get_fitness_cgi_decode import get_fitness_cgi_decode
from src.mutate import mutate
from src.selection import selection

generation: int = 0

def generateCrossovers(population, p_crossover, seed):
    crossovers = []
    for i in range(0, len(population), 2):
        if random.random() < p_crossover:
            offspring1, offspring2 = crossover(population[i], population[i + 1], seed)
            crossovers.append(offspring1)
            crossovers.append(offspring2)
        else:
            crossovers.append(population[i])
            crossovers.append(population[i + 1])
    return crossovers

def generateMutations(population, p_mutation, seed):
    mutations = []
    for i in range(0, len(population)):
        if random.random() < p_mutation:
            mutations.append(mutate(population[i], seed))
        else:
            mutations.append(population[i])
    return mutations

def coveredAllBranches(individual):
    get_fitness_cgi_decode(individual)
    coveredAll = True
    for i in range(1, 6):
        if i in distances_true.keys():
            coveredAll &= True
        else:
            coveredAll &= False
    clear_maps()
    return coveredAll

def getGeneration():
    return generation

def clearGeneration():
    global generation
    generation = 0
    return generation

def genetic_algorithm(seed=None):
    global generation
    population_size = 100
    tournament_size = 5
    p_crossover = 0.70
    p_mutation = 0.20

    # Generar y evaluar la poblacion inicial

    population = create_population(population_size, seed)
    evaluated_population = evaluate_population(population)

    # Imprimir el mejor valor de fitness encontrado
    best_individual_index, fitness_best_individual = selection(evaluated_population, tournament_size)
    best_individual = population[best_individual_index]
    print("Best fitness value: " + str(fitness_best_individual))

    # Continuar mientras la cantidad de generaciones es menor que 1000
    # y no haya ningun individuo que cubra todos los objetivos

    while generation < 1000 and not coveredAllBranches(best_individual):
        print("generation: ", generation)
        # Producir una nueva poblacion en base a la anterior.
        # Usar selection, crossover y mutation.
        new_population = generateMutations(generateCrossovers(population, p_crossover, seed), p_mutation, seed)

        # Una vez creada, reemplazar la poblacion anterior con la nueva
        generation += 1
        population = new_population

        # Evaluar la nueva poblacion e imprimir el mejor valor de fitness
        evaluated_population = evaluate_population(population)
        best_individual_index, fitness_best_individual = selection(evaluated_population, tournament_size)
        print("New best fitness value: " + str(fitness_best_individual))
        best_individual = population[best_individual_index]

    # retornar el mejor individuo de la ultima generacion
    return best_individual