import random
from src.create_population import create_population
from src.crossover import crossover
from src.evaluate_population import evaluate_population
from src.mutate import mutate
from src.selection import selection

generation: int = 0
seedUsed: int = 0
init_best_individual = []


def generateCrossovers(population, evaluated_population, p_crossover, population_size, tournament_size):
    crossovers = []
    while len(crossovers) < population_size:
        parent1Index, _ = selection(evaluated_population, tournament_size)
        parent2Index, _ = selection(evaluated_population, tournament_size)
        parent1 = population[parent1Index]
        parent2 = population[parent2Index]
        if random.random() < p_crossover:
            offspring1, offspring2 = crossover(parent1, parent2)
            crossovers.append(offspring1)
            crossovers.append(offspring2)
        else:
            crossovers.append(parent1)
            crossovers.append(parent2)
    return crossovers


def generateMutations(population, p_mutation):
    mutations = []
    for i in range(0, len(population)):
        if random.random() < p_mutation:
            mutations.append(mutate(population[i]))
        else:
            mutations.append(population[i])
    return mutations


def coveredAllBranches(fitness_individual):
    return fitness_individual == 0


def getGeneration():
    return generation


def getBestInitIndividual():
    return init_best_individual


def clearGeneration():
    global generation
    global seedUsed
    global init_best_individual
    generation = 0
    seedUsed = 0
    init_best_individual = []


def getBestIndividual(evaluated_population):
    best_individual_index = min(evaluated_population, key=evaluated_population.get)
    fitness_best_individual = evaluated_population[best_individual_index]
    return best_individual_index, fitness_best_individual

def getSeedUsed():
    return seedUsed


def genetic_algorithm(seed=None):
    global generation
    global seedUsed
    global init_best_individual
    seedUsed = seed
    population_size = 100
    tournament_size = 5
    p_crossover = 0.70
    p_mutation = 0.20

    # Generar y evaluar la poblacion inicial
    if seed is not None:
        random.seed(seed)
    population = create_population(population_size)
    evaluated_population = evaluate_population(population)

    # Imprimir el mejor valor de fitness encontrado
    best_individual_index, fitness_best_individual = getBestIndividual(evaluated_population)
    best_individual = population[best_individual_index]
    init_best_individual = best_individual

    # Continuar mientras la cantidad de generaciones es menor que 1000
    # y no haya ningun individuo que cubra todos los objetivos

    while generation < 1000 and not coveredAllBranches(fitness_best_individual):
        # Producir una nueva poblacion en base a la anterior.
        # Usar selection, crossover y mutation.
        new_population = generateMutations(generateCrossovers(population, evaluated_population, p_crossover, population_size, tournament_size), p_mutation)

        # Una vez creada, reemplazar la poblacion anterior con la nueva
        generation += 1
        population = new_population

        # Evaluar la nueva poblacion e imprimir el mejor valor de fitness
        evaluated_population = evaluate_population(population)
        best_individual_index, fitness_best_individual = getBestIndividual(evaluated_population)
        # print("New best fitness value: " + str(fitness_best_individual))
        best_individual = population[best_individual_index]

    # retornar el mejor individuo de la ultima generacion
    return best_individual