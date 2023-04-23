#!./venv/bin/python
import unittest

from src.genetic_algorithm import genetic_algorithm, getGeneration


class TestMutate(unittest.TestCase):
    def test1(self):
        genetic_algorithm(2)
        self.assertTrue(getGeneration() < 1000)
        self.assertTrue(getGeneration() > 0)

    def test2(self):
        # COMPLETAR
        pass

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