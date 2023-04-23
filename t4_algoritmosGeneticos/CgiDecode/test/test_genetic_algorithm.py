#!./venv/bin/python
import unittest

from src.genetic_algorithm import genetic_algorithm, getGeneration

# [i1,..., in] => [ i_k, i_j]

# cantidad de generaciones:
# 1) rompe a las 1000 iteraciones
# 2) rompe por que cubrio todos los branchs : test1
# fitness (3 .. n)
# 1) el individuo del algoritmo genetico es mejor que todos los individuos iniciales: (2 <3)
# 2) el individuo del algoritmo genetico esta rango dentro de la población inicial: (3 <= 4 <= n)
# 3) el individuo del algoritmo genetico es peor que todos los individuos iniciales: (n < n+1)
# branch coverage c1,..,ci,..,c5
# 1) el individuo del algoritmo genetico tiene mejor covertura de branch que la poblacion inicial
# 2) el individuo del algoritmo genetico tiene igual covertura de branch que la poblacion inicial
# 3) el individuo del algoritmo genetico tiene peor covertura de branch que la poblacion inicial

class TestMutate(unittest.TestCase):
    def test1(self):
        genetic_algorithm(2)
        print(getGeneration())
        self.assertTrue(getGeneration() < 1000)
        self.assertTrue(getGeneration() > 0)

    def testThereIsAndIndividualInTheInitialPopulationThatCoversAllTheBranches(self):
        genetic_algorithm(16)
        print(getGeneration())
        self.assertTrue(getGeneration() < 1000)
        self.assertEqual(getGeneration(), 0)

    # Este es el test que rompe, por que, la nueva poblacion es una lista vacia,
    # por ende no puede elegir el mejor individuo
    def testxxx(self):
        genetic_algorithm(18)
        print(getGeneration())

    def test2(self):
        for i in range(1, 100):
            genetic_algorithm(i)
            generation = getGeneration()
            print(f"seed: {i} y generacion: {generation}")


    def test3(self):
        # COMPLETAR
        pass

    def test4(self):
        # COMPLETAR
        pass

    def test5(self):
        # COMPLETAR
        pass

    def test6(self):
        # COMPLETAR
        pass

    def test7(self):
        # COMPLETAR
        pass

    def test8(self):
        # COMPLETAR
        pass

    def test9(self):
        # COMPLETAR
        pass

    def test10(self):
        # COMPLETAR
        pass