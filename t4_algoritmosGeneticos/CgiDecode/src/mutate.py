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
        modifiedCharIndex = getRandomCharIndex(testCase)
        individual[index] = testCase[:modifiedCharIndex] + getRandomChar() + testCase[modifiedCharIndex + 1:]
    else:
        testCase = individual[index]
        deletedCharIndex = getRandomCharIndex(testCase)
        individual[index] = testCase[:deletedCharIndex] + testCase[deletedCharIndex + 1:]
    return individual

def deleteTestCase(individual):
    individual.pop(getRandomFrom(individual))
    return individual

def getRandomCharIndex(testCase):
    charIndex = 0
    if testCase != "":
        charIndex = getRandomFrom(testCase)
    return charIndex
def getRandomFrom(individual):
    return random.randint(0, len(individual) - 1)

def mutate(individual, seed=None):
    mutatedIndividual = individual.copy()
    random.seed(seed)
    chosenOption = random.choices(options, equiprobability)[0]
    if chosenOption == "add":
        return addTestCase(mutatedIndividual)
    elif chosenOption == "modify":
        return modifyTestCase(mutatedIndividual)
    else:
        return deleteTestCase(mutatedIndividual)

