#!./venv/bin/python
import unittest

from src.create_population import create_population
from src.mutate import mutate


class TestMutate(unittest.TestCase):
    def testExample(self):
        population = create_population(1)
        mutate(population[0])
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(True, True)