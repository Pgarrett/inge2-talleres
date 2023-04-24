from typing import List, Set
from fuzzingbook.Coverage import Location
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner


class MagicFuzzer:


    def __init__(self, initial_inputs, function_to_call, function_name_to_call = None) -> None:
        self.function_name_to_call = function_name_to_call
        crashme_runner = FunctionCoverageRunner(function_to_call)
        self.initial_inputs = initial_inputs
        self.locationsPerInput = {}
        for input in self.initial_inputs:
            result, outcome = crashme_runner.run(input)
            locations = crashme_runner.coverage()
            locationsSet = set()
            for loc in locations:
                if loc[0] == self.function_name_to_call:
                    locationsSet.add(loc)
            self.locationsPerInput[input] = locationsSet

    def get_contributing_inputs(self) -> List[str]:
        coveredLocations = set()
        result = []
        for input in self.initial_inputs:
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
        """Aplica al azar alguna de las tres operaciones de mutacion definidas en el archivo mutation_utils.py"""
        pass

    def fuzz(self):
        """
        Elije aleatoriamente un input s usando seleccion de ruleta sobre e(s),
        muta el input s utilizando la función mutate(s), y ejecuta el s mutado
        """
        pass

    def run(self, n = None) -> int:
        """
        Corre una campaña del MagicFuzzer.
        La campaña debe ser ejecutada por n iteraciones (si n no es None), o hasta cubrir todas las líneas del programa.
        Retorna la cantidad de iteraciones realizadas.
        """
        pass