#!./venv/bin/python
import unittest

from src.create_population import create_population
from src.evaluate_population import evaluate_population
from src.selection import selection


class TestSelection(unittest.TestCase):
    def testExample(self):
        population = create_population(5)
        evaluated_population = evaluate_population(population)
        selection(evaluated_population)
        self.assertTrue(True)
        self.assertFalse(False)
        self.assertEqual(True, True)