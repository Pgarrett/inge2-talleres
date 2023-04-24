import random
from typing import Set
from fuzzingbook.Coverage import Location
from fuzzingbook.GreyboxFuzzer import getPathID


class RouletteInputSelector:

    def __init__(self, exponent: int):
        self.exponent = exponent
        self.inputsByPath = {}
        self.inputs = []

    def add_new_execution(self, s: str, s_path: Set[Location]):
        self.inputs.append(s)
        hash = getPathID(s_path)
        if hash in self.inputsByPath:
            self.inputsByPath[hash].append(s)
        else:
            l = []
            l.append(s)
            self.inputsByPath[hash] = l

    def get_frequency(self, s: str) -> int:
        for key in self.inputsByPath.keys():
            values = self.inputsByPath[key]
            if s in values:
                return len(values)
        return 0

    def get_energy(self, s: str) -> float:
        return 1/ (self.get_frequency(s)**self.exponent)

    def select(self) -> str:
        weights = []
        energyByInput = {}
        energySum = 0
        for input in self.inputs:
            energy = self.get_energy(input)
            energyByInput[input] = energy
            energySum += energy
        for input in self.inputs:
            weights.append((energyByInput[input]/energySum))
        return random.choices(self.inputs, weights=weights)[0]