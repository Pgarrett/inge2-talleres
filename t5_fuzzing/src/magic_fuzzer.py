import random
from typing import List, Set
from fuzzingbook.Coverage import Location
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner, insert_random_character, flip_random_character, \
    delete_random_character

from src.roulette_input_selector import RouletteInputSelector


class MagicFuzzer:

    def __init__(self, initial_inputs, function_to_call, function_name_to_call = None) -> None:
        self.function_name_to_call = function_name_to_call
        self.crashme_runner = FunctionCoverageRunner(function_to_call)
        self.executed_inputs = []
        self.locationsPerInput = {}
        for input in initial_inputs:
            self.doRun(input)

    def doRun(self, s: str):
        self.executed_inputs.append(s)
        self.crashme_runner.run(s)
        locations = self.crashme_runner.coverage()
        locationsSet = set()
        for loc in locations:
            if loc[0] == self.function_name_to_call:
                locationsSet.add(loc)
        self.locationsPerInput[s] = locationsSet

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
        selector = RouletteInputSelector(2)
        for input in self.executed_inputs:
            selector.add_new_execution(input, self.locationsPerInput[input])
        mutated = self.mutate(selector.select())
        self.doRun(mutated)

    def run(self, n = None) -> int:
        """
        Corre una campaña del MagicFuzzer.
        La campaña debe ser ejecutada por n iteraciones (si n no es None), o hasta cubrir todas las líneas del programa.
        Retorna la cantidad de iteraciones realizadas.
        """
        pass