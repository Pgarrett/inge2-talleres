#!./venv/bin/python
import random
import unittest

from src.create_population import create_population
from src.crossover import crossover
from src.evaluate_condition import clear_maps


class TestCrossover(unittest.TestCase):

    def setUp(self):
        clear_maps()

    def testWithPredefinedPopulation(self):
        population = [["Hello+Reader", "", "Hello+R%eader", "+"], ["%AA", "%1", "&&&", "%AU", "1", "2432sa145.l", "[]", "qerasdfb", "12345678"]]
        offspring1, offspring2 = crossover(population[0], population[1], 2)
        crossoverLimit = random.randint(1, min(len(population[0]), len(population[1])))
        self.assertEqual(offspring1, population[0][0:crossoverLimit] + population[1][crossoverLimit:])
        self.assertEqual(offspring2, population[1][0:crossoverLimit] + population[0][crossoverLimit:])

    def testRandomPopulation(self):
        population = create_population(2)
        offspring1, offspring2 = crossover(population[0], population[1], 2)
        crossoverLimit = random.randint(1, min(len(population[0]), len(population[1])))
        self.assertEqual(offspring1, population[0][0:crossoverLimit] + population[1][crossoverLimit:])
        self.assertEqual(offspring2, population[1][0:crossoverLimit] + population[0][crossoverLimit:])