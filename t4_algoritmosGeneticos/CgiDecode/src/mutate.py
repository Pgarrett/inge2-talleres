import random

from src.create_population import getRandomString, getRandomChar

options = ["add", "modify", "delete"]
equiprobability = [1/3, 1/3, 1/3]
def addTestCase(individual):
    individual.append(getRandomString())
    return individual

def modifyTestCase(individual):
    chosenOption = random.choices(options, equiprobability)[0]
    index = getRandomFrom(individual)
    if chosenOption == "add":
        individual[index] = individual[index] + getRandomChar()
    elif chosenOption == "modify":
        testCase = individual[index]
        if testCase != "":
            modifiedCharIndex = getRandomCharIndex(testCase)
            individual[index] = testCase[:modifiedCharIndex] + getRandomChar() + testCase[modifiedCharIndex + 1:]
        else:
            individual[index] = individual[index] + getRandomChar()
    else:
        testCase = individual[index]
        if testCase != "":
            deletedCharIndex = getRandomCharIndex(testCase)
            individual[index] = testCase[:deletedCharIndex] + testCase[deletedCharIndex + 1:]
    return individual

# Como el individuo sin casos de test no lo consideramos valido,
# solo borramos un elemento si el individuo tiene mas de un caso de test
def deleteTestCase(individual):
    if len(individual) > 1:
        individual.pop(getRandomFrom(individual))
    return individual

def getRandomCharIndex(testCase):
    return getRandomFrom(testCase) if testCase != "" else 0
def getRandomFrom(individual):
    return random.randint(0, len(individual) - 1)

def mutate(individual, seed=None):
    mutatedIndividual = individual.copy()
    if seed is not None:
        random.seed(seed)
    chosenOption = random.choices(options, equiprobability)[0]
    if chosenOption == "add":
        return addTestCase(mutatedIndividual)
    elif chosenOption == "modify":
        return modifyTestCase(mutatedIndividual)
    else:
        return deleteTestCase(mutatedIndividual)

