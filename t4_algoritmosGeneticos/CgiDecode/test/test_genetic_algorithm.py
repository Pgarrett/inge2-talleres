#!./venv/bin/python
import unittest

from src.genetic_algorithm import genetic_algorithm, getGeneration, clearGeneration, bestFitnessIniPopulation, worstFitnessIniPopulation
from src.get_fitness_cgi_decode import get_fitness_cgi_decode

# [i1,..., in] => [ i_k, i_j]

# cantidad de generaciones:
# 1) Sale del while por que cubrio todos los branchs pero con generaciones posterioores : test1
# 2) Sale del while por que cubrio todos los branchs pero con la poblacion inicial : test2
# 3) Sale del while por que se le acabo el presupuesto test3
# fitness (3 .. n)
# 1) el individuo del algoritmo genetico es mejor que todos los individuos iniciales: (2 <3): test4
# 2) el individuo del algoritmo genetico esta rango dentro de la población inicial: (3 <= 4 <= n): test5
# 3) el individuo del algoritmo genetico es peor que todos los individuos iniciales: (n < n+1)
# branch coverage c1,..,ci,..,c5
# 1) el individuo del algoritmo genetico tiene mejor covertura de branch que la poblacion inicial
# 2) el individuo del algoritmo genetico tiene igual covertura de branch que la poblacion inicial
# 3) el individuo del algoritmo genetico tiene peor covertura de branch que la poblacion inicial

class TestMutate(unittest.TestCase):

    def setUp(self):
        clearGeneration()

    def test1(self):
        genetic_algorithm(5)
        self.assertTrue(getGeneration() < 1000)
        self.assertTrue(getGeneration() > 0)

    def test2(self):
        genetic_algorithm(16)
        self.assertTrue(getGeneration() < 1000)
        self.assertEqual(getGeneration(), 0)

    def test3(self):
        genetic_algorithm(11)
        self.assertEqual(getGeneration(), 1000)

    def test4(self):
        bestIndividual = genetic_algorithm(135)
        bestFitness = get_fitness_cgi_decode(bestIndividual)
        self.assertTrue(bestFitnessIniPopulation() > bestFitness)

    def test5(self):
        bestIndividual = genetic_algorithm(16)
        bestFitness = get_fitness_cgi_decode(bestIndividual)
        self.assertTrue(bestFitnessIniPopulation() <= bestFitness)
        self.assertTrue(worstFitnessIniPopulation() >= bestFitness)

    # def test6(self):
    #     # COMPLETAR
    #     pass
    #
    # def test7(self):
    #     # COMPLETAR
    #     pass
    #
    # def test8(self):
    #     # COMPLETAR
    #     pass
    #
    # def test9(self):
    #     # COMPLETAR
    #     pass
    #
    # def test10(self):
    #     # COMPLETAR
    #     pass