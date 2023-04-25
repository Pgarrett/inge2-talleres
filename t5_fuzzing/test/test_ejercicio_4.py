#!./venv/bin/python
import random
import unittest

from src.crashme import crashme
from src.magic_fuzzer import MagicFuzzer


class TestEjercicio4(unittest.TestCase):

    # En mi compu tardo 1 minuto 44 segundos, una ganga
    def testRunning5IterationsGeneratesNewCoveredLocations(self):
        inputs = [" "]
        iters = []
        seeds = [2, 3, 4, 7, 8]
        for campaign in range(0, 5):
            random.seed(seeds[campaign])
            fuzzer = MagicFuzzer(inputs, crashme, function_name_to_call="crashme")
            iters.append(fuzzer.run())
        self.assertEqual(iters, [2957, 1618, 550, 1828, 2066])
