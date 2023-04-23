#!./venv/bin/python
import unittest

from src.create_population import create_population
from src.mutate import mutate


class TestMutate(unittest.TestCase):

    # Despues de un par de corridas con distintos seeds,
    # encontramos que los siguientes seeds satisfacen los casos que necesitamos
    # 0 -> delete
    # 1 -> add
    # 5 -> modify[delete]
    # 9 -> modify[modify]
    # 30 -> modify[add]

    def hasEmptyTestCase(self, individual):
        result = False
        for case in individual:
            result |= (case == "")
        return result

    def ensurePopulationWithNonEmptyTestCase(self):
        population = create_population(1)
        while self.hasEmptyTestCase(population[0]):
            population = create_population(1)
        return population

    def getLengthsFrom(self, list):
        lengths = []
        for i in range(0, len(list)):
            lengths.append(len(list[i]))
        return lengths

    def testNoCaseIsDeletedWhenIndividualHasOnlyOneTestCase(self):
        population = [["hello"]]
        originalLength = len(population[0])
        modifiedIndividual = mutate(population[0], 0)
        self.assertEqual(len(modifiedIndividual), originalLength)

    def testDeleteCaseFromIndividual(self):
        population = create_population(1)
        originalLength = len(population[0])
        modifiedIndividual = mutate(population[0], 0)
        self.assertEqual(len(modifiedIndividual), originalLength - 1)

    def testAddCaseToIndividual(self):
        population = create_population(1)
        originalLength = len(population[0])
        modifiedIndividual = mutate(population[0], 1)
        self.assertEqual(len(modifiedIndividual), originalLength + 1)

    def testModifyCaseToIndividual(self):
        population = create_population(1)
        originalLength = len(population[0])
        modifiedIndividual = mutate(population[0], 5)
        self.assertEqual(len(modifiedIndividual), originalLength)

    def testModifyCharToEmtpyTestCaseAddsChar(self):
        population = [[""]]
        individual = population[0]
        originalLengths = self.getLengthsFrom(individual)
        modifiedIndividual = mutate(population[0], 9)
        modifiedLengths = self.getLengthsFrom(modifiedIndividual)
        changedLengths = 0
        for i in range(0, len(individual)):
            if originalLengths[i] != modifiedLengths[i]:
                changedLengths += 1
        self.assertEqual(changedLengths, 1)
        self.assertEqual(originalLengths[0], modifiedLengths[0] - 1)

    def testAddCharToEmtpyTestCaseAddsChar(self):
        population = [[""]]
        individual = population[0]
        originalLengths = self.getLengthsFrom(individual)
        modifiedIndividual = mutate(population[0], 30)
        modifiedLengths = self.getLengthsFrom(modifiedIndividual)
        changedLengths = 0
        for i in range(0, len(individual)):
            if originalLengths[i] != modifiedLengths[i]:
                changedLengths += 1
        self.assertEqual(changedLengths, 1)
        self.assertEqual(originalLengths[0], modifiedLengths[0] - 1)

    def testAddCharToTestCase(self):
        population = create_population(1)
        individual = population[0]
        originalLengths = self.getLengthsFrom(individual)
        modifiedIndividual = mutate(population[0], 30)
        modifiedLengths = self.getLengthsFrom(modifiedIndividual)
        changedLengths = 0
        changedCase = -1
        for i in range(0, len(individual)):
            if originalLengths[i] != modifiedLengths[i]:
                changedLengths += 1
                changedCase = i
        self.assertEqual(changedLengths, 1)
        self.assertEqual(originalLengths[changedCase], modifiedLengths[changedCase] - 1)

    def testDeleteCharToEmptyTestCaseDoesNothing(self):
        population = [[""]]
        individual = population[0]
        originalLengths = self.getLengthsFrom(individual)
        modifiedIndividual = mutate(population[0], 5)
        modifiedLengths = self.getLengthsFrom(modifiedIndividual)
        lengthsDoNotChange = True
        for i in range(0, len(individual)):
            lengthsDoNotChange &= (originalLengths[i] == modifiedLengths[i])
        self.assertTrue(lengthsDoNotChange)
        self.assertEqual(originalLengths, modifiedLengths)

    def testDeleteCharFromTestCase(self):
        population = self.ensurePopulationWithNonEmptyTestCase()
        individual = population[0]
        originalLengths = self.getLengthsFrom(individual)
        modifiedIndividual = mutate(population[0], 5)
        modifiedLengths = self.getLengthsFrom(modifiedIndividual)
        changedLengths = 0
        changedCase = -1
        for i in range(0, len(individual)):
            if originalLengths[i] != modifiedLengths[i]:
                changedLengths += 1
                changedCase = i
        self.assertEqual(changedLengths, 1)
        self.assertEqual(originalLengths[changedCase], modifiedLengths[changedCase] + 1)

    def testModifyCharFromTestCase(self):
        population = self.ensurePopulationWithNonEmptyTestCase()
        individual = population[0]
        originalLengths = self.getLengthsFrom(individual)
        modifiedIndividual = mutate(population[0], 9)
        modifiedLengths = self.getLengthsFrom(modifiedIndividual)
        changedCase = -1
        for i in range(0, len(individual)):
            if individual[i] != modifiedIndividual[i]:
                changedCase = i
        self.assertEqual(originalLengths, modifiedLengths)
        self.assertNotEqual(individual[changedCase], modifiedIndividual[changedCase])