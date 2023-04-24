#!./venv/bin/python
import unittest

from src.evaluate_condition import clear_maps
from src.genetic_algorithm import genetic_algorithm, getGeneration, clearGeneration, bestFitnessIniPopulation, \
    getEndBranchCoverage, getInitBranchCoverage
from src.get_fitness_cgi_decode import get_fitness_cgi_decode

# [i1,..., in] => [ i_k, i_j]

# cantidad de generaciones:
# 1) Sale del while por que cubrio todos los branchs pero con generaciones posterioores : test1
# 2) Sale del while por que cubrio todos los branchs pero con la poblacion inicial : test2
# 3) Sale del while por que se le acabo el presupuesto test3
# fitness
# 1) El individuo del algoritmo genetico su valor de fitness es mejor que el mejor valor de fitness individuo de la poblacion inicial: test4
# 2) El individuo del algoritmo genetico su valor de fitness es igual que el mejor valor de fitness individuo de la poblacion inicial: test5
# 3) El individuo del algoritmo genetico su valor de fitness es peor que el mejor valor de fitness individuo de la poblacion inicial: test6
# branch coverage c1,..,ci,..,c5
# 1) el individuo del algoritmo genetico tiene mejor covertura de branch que la poblacion inicial
# 2) el individuo del algoritmo genetico tiene igual covertura de branch que la poblacion inicial
# 3) el individuo del algoritmo genetico tiene peor covertura de branch que la poblacion inicial
# random
# 1) dos generaciones distintas dan individuos distintos

class TestGenetic(unittest.TestCase):

    def setUp(self):
        clearGeneration()
        clear_maps()

    def testExecutesMoreThanOneGeneration(self):
        genetic_algorithm(5)
        self.assertTrue(getGeneration() < 1000)
        self.assertTrue(getGeneration() > 0)

    def testInitialPopulationCoversAllTargets(self):
        genetic_algorithm(16)
        self.assertTrue(getGeneration() < 1000)
        self.assertEqual(getGeneration(), 0)

    def test1000GenerationsAreNotEnough(self):
        genetic_algorithm(11)
        self.assertEqual(getGeneration(), 1000)

    def testGeneticResultHasBetterFitnessThanBestInitialPopulation(self):
        bestIndividual = genetic_algorithm(135)
        bestFitness = get_fitness_cgi_decode(bestIndividual)
        self.assertTrue(bestFitnessIniPopulation() > bestFitness)

    def testGeneticResultHasEqualFitnessThanBestInitialPopulation(self):
        bestIndividual = genetic_algorithm(29)
        bestFitness = get_fitness_cgi_decode(bestIndividual)
        self.assertEqual(bestFitnessIniPopulation(), bestFitness)

    def testGeneticResultHasWorseFitnessThanBestInitialPopulation(self):
        bestIndividual = genetic_algorithm(16)
        bestFitness = get_fitness_cgi_decode(bestIndividual)
        self.assertTrue(bestFitnessIniPopulation() < bestFitness)

    def testInitialCoverageIsWorseThanGeneticResult(self):
        genetic_algorithm(0)
        self.assertTrue(getInitBranchCoverage() < getEndBranchCoverage())

    def testInitialCoverageIsEqualToGeneticResult(self):
        genetic_algorithm(4)
        self.assertEqual(getInitBranchCoverage(), getEndBranchCoverage())

    def testInitialCoverageIsBetterThanGeneticResult(self):
        genetic_algorithm(62)
        self.assertTrue(getInitBranchCoverage() > getEndBranchCoverage())

    def testUsingNoSeedGeneratesDifferentIndividuals(self):
        firstIndividual = genetic_algorithm()
        secondIndividual = genetic_algorithm()
        self.assertNotEqual(firstIndividual, secondIndividual)
