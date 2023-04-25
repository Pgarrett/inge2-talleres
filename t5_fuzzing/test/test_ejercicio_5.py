#!./venv/bin/python
import datetime
import unittest
import random

from src.magic_fuzzer import MagicFuzzer
from src.my_parser import my_parser


class TestEjercicio5(unittest.TestCase):

    def test(self):
        inputs = [" "]
        linesCovered = []
        seeds = [2, 3, 4, 7, 8]
        for campaign in range(0, 5):
            random.seed(seeds[campaign])
            fuzzer = MagicFuzzer(inputs, my_parser)
            fuzzer.run(5000)
            linesCovered.append(len(fuzzer.get_covered_locations()))
        self.assertEqual(linesCovered, [93, 88, 88, 89, 88])