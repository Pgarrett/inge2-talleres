import random
import string

# Consideramos que una lista vacia no es un individuo valido. Por otro lado, un test case como string vacio si lo es
def create_population(population_size, seed=None):
    random.seed(seed)
    population = []
    if population_size < 0:
        population_size = 0
    for i in range(0, population_size):
        population.append(getRandomList())
    return population

def getRandomList():
    randomList = []
    listSize = random.randint(1, 15)
    for i in range(0, listSize):
        randomList.append(getRandomString())
    return randomList

def getRandomString():
    stringSize = random.randint(0, 10)
    return ''.join(getRandomChar() for _ in range(stringSize))

def getRandomChar():
    characters = string.ascii_letters + string.digits + '''!()-[]{};:,<>.?@#$%^&*_~'''
    return random.choice(characters)