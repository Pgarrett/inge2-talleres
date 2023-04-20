#!./venv/bin/python
import unittest

from src.create_population import create_population
from src.evaluate_condition import clear_maps
from src.evaluate_population import evaluate_population
from src.get_fitness_cgi_decode import get_fitness_cgi_decode
from src.selection import selection


class TestSelection(unittest.TestCase):

    def setUp(self):
        clear_maps()

    def testWithPredefinedPopulation(self):
        population = [["Hello+Reader", "", "Hello+R%eader", "+"], ["%AA"]]
        evaluated_population = evaluate_population(population)
        winnerIndex, winnerScore = selection(evaluated_population, 4)
        self.assertEqual(winnerIndex, 0)
        self.assertEqual(winnerScore, 1)

    def testTournamentWinnerBelongsToPopulation(self):
        population = create_population(5, 10)
        evaluated_population = evaluate_population(population)
        winnerIndex, winnerScore = selection(evaluated_population, 4)
        self.assertTrue(winnerIndex < len(population))
        self.assertEqual(winnerScore, get_fitness_cgi_decode(population[winnerIndex]))