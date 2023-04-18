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
        self.assertEqual(evaluatedPopulation[population[0]], (35/36)+2)
        self.assertEqual(evaluatedPopulation[population[1]], 4.5)
        self.assertEqual(evaluatedPopulation[population[2]], 1.5)
        self.assertEqual(evaluatedPopulation[population[3]], 3.5)

    def testCreateRandomPopulation(self):
        population = create_population(5)
        evaluatedPopulation = evaluate_population(population)
        for member in population:
            self.assertEqual(evaluatedPopulation[member], get_fitness_cgi_decode([member]))