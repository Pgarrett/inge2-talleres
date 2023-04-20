#!./venv/bin/python
import unittest

from src.create_population import create_population
from src.crossover import crossover


class TestCrossover(unittest.TestCase):

    def testWithPredefinedPopulation(self):
        population = [["Hello+Reader", "", "Hello+R%eader", "+"], ["%AA", "%1", "&&&"]]
        offspring1, offspring2 = crossover(population[0], population[1], 2)
        print(offspring1)
        print(offspring2)
        # self.assertEqual(winnerIndex, 0)
        # self.assertEqual(winnerScore, 1)

    def testExample(self):
        population = create_population(2)
        crossover(population[0], population[1])
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(True, True)