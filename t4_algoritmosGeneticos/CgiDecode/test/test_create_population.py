#!./venv/bin/python
import unittest
from src.create_population import create_population


class TestCreatePopulation(unittest.TestCase):

    def testNegativePopulationReturnsNoPopulation(self):
        population = create_population(-1)
        self.assertEqual(len(population), 0)

    def testNewPopulationRespectsSizeOfLess15(self):
        population = create_population(10)
        self.assertEqual(len(population), 10)

    def testNewPopulationIsMaxOf15Cases(self):
        population = create_population(20)
        self.assertEqual(len(population), 15)

    def testAllMembersOfPopulationAreLessThan10CharactersLong(self):
        population = create_population(12)
        for member in population:
            self.assertTrue(len(member) <= 10)