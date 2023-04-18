def genetic_algorithm(seed=None):
    population_size = 100
    tournament_size = 5
    p_crossover = 0.70
    p_mutation = 0.20

    # Generar y evaluar la poblacion inicial
    generation = 0

    population = None # COMPLETAR
    evaluated_population = None # COMPLETAR

    # Imprimir el mejor valor de fitness encontrado
    best_individual = None # COMPLETAR
    fitness_best_individual = None # COMPLETAR

    # Continuar mientras la cantidad de generaciones es menor que 1000
    # y no haya ningun individuo que cubra todos los objetivos

    while True: # COMPLETAR

        # Producir una nueva poblacion en base a la anterior.
        # Usar selection, crossover y mutation.
        new_population = None # COMPLETAR

        # Una vez creada, reemplazar la poblacion anterior con la nueva
        generation += 1
        population = new_population

        # Evaluar la nueva poblacion e imprimir el mejor valor de fitness
        evaluated_population = None # COMPLETAR
        best_individual = None # COMPLETAR
        fitness_best_individual = None # COMPLETAR

    # retornar el mejor individuo de la ultima generacion
    return best_individual