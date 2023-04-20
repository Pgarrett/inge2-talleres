import random
import string

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
    listSize = random.randint(0, 15)
    for i in range(0, listSize):
        randomList.append(getRandomString())
    return randomList

def getRandomString():
    stringSize = random.randint(0, 10)
    characters = string.ascii_letters + string.digits + '''!()-[]{};:,<>.?@#$%^&*_~'''
    return ''.join(random.choice(characters) for _ in range(stringSize))