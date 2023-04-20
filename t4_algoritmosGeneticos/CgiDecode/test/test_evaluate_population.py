#!./venv/bin/python
import unittest
from src.create_population import create_population
from src.evaluate_population import evaluate_population
from src.evaluate_condition import clear_maps
from src.get_fitness_cgi_decode import get_fitness_cgi_decode


class TestEvaluatePopulation(unittest.TestCase):

    def setUp(self):
        clear_maps()

    def testCreatePopulation(self):
        population = [["Hello+Reader", "", "Hello+R%eader", "+"]]
        evaluatedPopulation = evaluate_population(population)
        self.assertEqual(evaluatedPopulation[0], 1)

    def testCreateRandomPopulation(self):
        population = create_population(5)
        evaluatedPopulation = evaluate_population(population)

        for i in range(0, len(population)):
            clear_maps()
            self.assertEqual(evaluatedPopulation[i], get_fitness_cgi_decode(population[i]))