import random
from typing import List, Set
from fuzzingbook.Coverage import Location
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner, insert_random_character, flip_random_character, \
    delete_random_character

from src.roulette_input_selector import RouletteInputSelector


class MagicFuzzer:

    def __init__(self, initial_inputs, function_to_call, function_name_to_call = None) -> None:
        self.maxCoverage = 0
        self.function_name_to_call = function_name_to_call
        self.crashme_runner = FunctionCoverageRunner(function_to_call)
        self.executed_inputs = []
        self.locationsPerInput = {}
        self.selector = RouletteInputSelector(2)
        for input in initial_inputs:
            self.doRun(input)

    def doRun(self, s: str):
        self.executed_inputs.append(s)
        self.crashme_runner.run(s)
        locations = self.crashme_runner.coverage()
        locationsSet = set()
        for loc in locations:
            if self.function_name_to_call is not None:
                if loc[0] == self.function_name_to_call:
                    locationsSet.add(loc)
            else:
                locationsSet.add(loc)
        self.locationsPerInput[s] = locationsSet
        self.selector.add_new_execution(s, locationsSet)

    def get_contributing_inputs(self) -> List[str]:
        coveredLocations = set()
        result = []
        for input in self.executed_inputs:
            inputLocations = self.locationsPerInput[input]
            for loc in inputLocations:
                if loc not in coveredLocations:
                    if input not in result:
                        result.append(input)
                    coveredLocations.add(loc)
        return result

    def get_covered_locations(self) -> Set[Location]:
        maxCoveredLocations = set()
        for key in self.locationsPerInput.keys():
                if len(self.locationsPerInput[key]) > len(maxCoveredLocations):
                    maxCoveredLocations = self.locationsPerInput[key]
        return maxCoveredLocations

    def mutate(self, s: str) -> str:
        optionChosen = random.choices(["add", "flip", "delete"])[0]
        if optionChosen == "add":
            return insert_random_character(s)
        elif optionChosen == "flip":
            return flip_random_character(s)
        else:
            return delete_random_character(s)

    def fuzz(self):
        mutated = self.mutate(self.selector.select())
        self.doRun(mutated)

    def run(self, n = None) -> int:
        if n is None:
            iteration = 1
            while not self.campaignCoveredAllCrashMe():
                iteration += 1
            return iteration
        else:
            for i in range(0, n):
                self.fuzz()
            return n

    def campaignCoveredAllCrashMe(self):
        self.fuzz()
        for key in self.locationsPerInput.keys():
            if len(self.locationsPerInput[key]) == 5:
                return True
        return False

    def allCrashMeHaveBeenIterated(self, locations: Set[Location]):
        crashMeLines = [("crashme", 6), ("crashme", 7), ("crashme", 8), ("crashme", 9), ("crashme", 10)]
        result = True
        for line in crashMeLines:
            result &= line in locations
        return result