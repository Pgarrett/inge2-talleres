#!./venv/bin/python
import unittest
from src.get_fitness_cgi_decode import get_fitness_cgi_decode
from src.evaluate_condition import clear_maps


class TestGetFitnessCgiDecode(unittest.TestCase):

    def setUp(self):
        clear_maps()

    def testAA(self):
        fitness = get_fitness_cgi_decode(["%AA"])
        self.assertEqual(fitness, 2.857142857142857)

    def testAU(self):
        fitness = get_fitness_cgi_decode(["%AU"])
        self.assertEqual(fitness, 3.607142857142857)

    def testUU(self):
        fitness = get_fitness_cgi_decode(["%UU"])
        self.assertEqual(fitness, 4.03021978021978)

    def testHelloReader(self):
        fitness = get_fitness_cgi_decode(["Hello+Reader"])
        self.assertEqual(fitness, (35/36)+2)

    def testEmtpyString(self):
        fitness = get_fitness_cgi_decode([""])
        self.assertEqual(fitness, 4.5)

    def testPercentage(self):
        fitness = get_fitness_cgi_decode(["%"])
        self.assertEqual(fitness, 3.857142857142857)

    def testPercentage1(self):
        fitness = get_fitness_cgi_decode(["%1"])
        self.assertEqual(fitness, 4.023809523809524)

    def testPlus(self):
        fitness = get_fitness_cgi_decode(["+"])
        self.assertEqual(fitness, 3.5)

    def testPlusPercentage1(self):
        fitness = get_fitness_cgi_decode(["+%1"])
        self.assertEqual(fitness, 3.1666666666666665)

    def testPercentage1Plus(self):
        fitness = get_fitness_cgi_decode(["%1+"])
        self.assertEqual(fitness, 3.607142857142857)

    def testTwoStrings(self):
        fitness = get_fitness_cgi_decode(["Hello+Reader", "AguanteInge2"])
        self.assertEqual(fitness, 2.928571428571429)

    def testStringWithAllConditions(self):
        fitness = get_fitness_cgi_decode(["Hello+R%eader"])
        self.assertEqual(fitness, 1.5)