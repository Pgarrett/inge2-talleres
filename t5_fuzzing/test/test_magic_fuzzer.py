#!./venv/bin/python
import random
import unittest

from fuzzingbook.MutationFuzzer import mutate

from src.magic_fuzzer import MagicFuzzer
from src.crashme import crashme
from parameterized import parameterized


class TestMagicFuzzer(unittest.TestCase):

    @parameterized.expand([
        [[], [], []],
        [["good"], [("crashme", 6)], ["good"]],
        [["bad!"], [("crashme", 6), ("crashme", 7), ("crashme", 8), ("crashme", 9), ("crashme", 10)], ["bad!"]],
        [["good", "goo"], [("crashme", 6)], ["good"]],
        [["good", "bad!"], [("crashme", 6), ("crashme", 7), ("crashme", 8), ("crashme", 9), ("crashme", 10)], ["good", "bad!"]],
        [["bad!", "good"], [("crashme", 6), ("crashme", 7), ("crashme", 8), ("crashme", 9), ("crashme", 10)], ["bad!"]],
        [["good", "b", "ba"], [("crashme", 6), ("crashme", 7), ("crashme", 8)], ["good", "b", "ba"]],
        [["good", "b", "bad!"], [("crashme", 6), ("crashme", 7), ("crashme", 8), ("crashme", 9), ("crashme", 10)], ["good", "b", "bad!"]],
        [["good", "go", "b", "bad!"], [("crashme", 6), ("crashme", 7), ("crashme", 8), ("crashme", 9), ("crashme", 10)], ["good", "b", "bad!"]],
    ])
    def test(self, inputs, expected_covered_locations, expected_contributing_inputs):
        fuzzer = MagicFuzzer(inputs, crashme, function_name_to_call="crashme")
        self.assertSetEqual(fuzzer.get_covered_locations(), set(expected_covered_locations))
        self.assertListEqual(fuzzer.get_contributing_inputs(), expected_contributing_inputs)

    def testMutateDeletesInString(self):
        random.seed(2)
        mutated = mutate("Hello World")
        self.assertEqual(mutated, "Hllo World")

    def testMutateModifyInString(self):
        random.seed(5)
        mutated = mutate("Hello World")
        self.assertEqual(mutated, "HellO World")

    def testMutateAddsInString(self):
        random.seed(7)
        mutated = mutate("Hello World")
        self.assertEqual(mutated, "HeRllo World")

    def testFuzzingInputIncreasesCoverage(self):
        random.seed(4259)
        inputs = ["good"]
        fuzzer = MagicFuzzer(inputs, crashme, function_name_to_call="crashme")
        fuzzer.fuzz()
        self.assertSetEqual(fuzzer.get_covered_locations(), set([("crashme", 6), ("crashme", 7)]))
        self.assertListEqual(fuzzer.get_contributing_inputs(), ["good", "bgood"])
