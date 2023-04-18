import random
import string

def create_population(population_size, seed=None):
    random.seed(seed)
    if population_size < 0:
        population_size = 0
    for i in range(0, population_size):
        getRandomList()
    return population

def getRandomList():
    randomList = []
    listSize = random.randint(1, 15)
    for i in range(0, listSize):
        population.append(getRandomString())

def getRandomString():
    stringSize = random.randint(1, 10)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(stringSize))