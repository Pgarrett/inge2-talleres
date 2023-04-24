#!./venv/bin/python
import random
import unittest

from src.crashme import crashme
from src.magic_fuzzer import MagicFuzzer


class TestEjercicio4(unittest.TestCase):

    def testRunning5IterationsGeneratesNewCoveredLocations(self):
        inputs = [" "]
        fuzzer = MagicFuzzer(inputs, crashme, function_name_to_call="crashme")
        self.assertSetEqual(fuzzer.get_covered_locations(), set([("crashme", 6)]))
        self.assertListEqual(fuzzer.get_contributing_inputs(), inputs)
        random.seed(32)
        fuzzer.run(5)
        self.assertSetEqual(fuzzer.get_covered_locations(), set([("crashme", 6), ("crashme", 7)]))
        self.assertListEqual(fuzzer.get_contributing_inputs(), [" ", "b "])