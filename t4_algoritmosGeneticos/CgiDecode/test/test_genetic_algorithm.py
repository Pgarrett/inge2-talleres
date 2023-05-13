#!./venv/bin/python
import unittest

from src.evaluate_condition import clear_maps, distances_true, distances_false
from src.genetic_algorithm import genetic_algorithm, getGeneration, clearGeneration, getSeedUsed
from src.get_fitness_cgi_decode import get_fitness_cgi_decode


class TestGenetic(unittest.TestCase):

    def setUp(self):
        clearGeneration()
        clear_maps()

    def getFitnessAndBranchCoverage(self, individual):
        fitness = get_fitness_cgi_decode(individual)
        branchCoverage = self.branchCoverageFor()
        clear_maps()
        return fitness, branchCoverage
    def branchCoverageFor(self):
        coveredUpTo = 1
        for i in range(1, 4):
            if i in distances_true.keys() and distances_true[i] == 0:
                coveredUpTo += 1
            if i in distances_false.keys() and distances_false[i] == 0:
                coveredUpTo += 1
        if 4 in distances_true.keys() and 5 in distances_true.keys() and distances_true[4] == 0 and distances_true[5] == 0:
            coveredUpTo += 1
        if 4 not in distances_false.keys() or 5 not in distances_false.keys() or distances_true[4] != 0 or distances_true[5] != 0:
            coveredUpTo += 1
        return coveredUpTo/8

    def test1(self):
        result = genetic_algorithm(1)
        self.assertEqual(getSeedUsed(), 1)
        self.assertEqual(getGeneration(), 1)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test2(self):
        result = genetic_algorithm(945)
        self.assertEqual(getSeedUsed(), 945)
        self.assertEqual(getGeneration(), 2)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test3(self):
        result = genetic_algorithm(3)
        self.assertEqual(getSeedUsed(), 3)
        self.assertEqual(getGeneration(), 4)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test4(self):
        result = genetic_algorithm(4)
        self.assertEqual(getSeedUsed(), 4)
        self.assertEqual(getGeneration(), 3)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test5(self):
        result = genetic_algorithm(5)
        self.assertEqual(getSeedUsed(), 5)
        self.assertEqual(getGeneration(), 1)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test6(self):
        result = genetic_algorithm(6)
        self.assertEqual(getSeedUsed(), 6)
        self.assertEqual(getGeneration(), 18)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test7(self):
        result = genetic_algorithm(7)
        self.assertEqual(getSeedUsed(), 7)
        self.assertEqual(getGeneration(), 3)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test8(self):
        result = genetic_algorithm(8)
        self.assertEqual(getSeedUsed(), 8)
        self.assertEqual(getGeneration(), 2)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test9(self):
        result = genetic_algorithm(9)
        self.assertEqual(getSeedUsed(), 9)
        self.assertEqual(getGeneration(), 3)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)

    def test10(self):
        result = genetic_algorithm(10)
        self.assertEqual(getSeedUsed(), 10)
        self.assertEqual(getGeneration(), 3)
        fitness, branchCoverage = self.getFitnessAndBranchCoverage(result)
        self.assertEqual(fitness, 0)
        self.assertEqual(branchCoverage, 1)