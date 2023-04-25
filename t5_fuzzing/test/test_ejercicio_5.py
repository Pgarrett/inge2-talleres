#!./venv/bin/python
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
            print("running campaign: " + str(campaign))
            random.seed(seeds[campaign])
            fuzzer = MagicFuzzer(inputs, my_parser)
            fuzzer.run()
            linesCovered.append(self.getMyParserLocations())
        self.assertEqual(linesCovered, [2957, 1618, 550, 1828, 2066])

    def getMyParserLocations(self, fuzzer: MagicFuzzer):
        locations = fuzzer.get_covered_locations()
        parser_locations = set()
        for location in locations:
            if location[0] == "my_parser":
                parser_locations.add(location)
        return len(parser_locations)