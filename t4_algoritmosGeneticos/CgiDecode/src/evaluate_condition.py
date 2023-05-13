import sys
from typing import Dict

# Inicializar mappings globales
distances_true: Dict[int, int] = {}
distances_false: Dict[int, int] = {}


def update_maps(condition_num, d_true, d_false):
    global distances_true, distances_false

    if condition_num in distances_true.keys():
        distances_true[condition_num] = min(
            distances_true[condition_num], d_true)
    else:
        distances_true[condition_num] = d_true

    if condition_num in distances_false.keys():
        distances_false[condition_num] = min(
            distances_false[condition_num], d_false)
    else:
        distances_false[condition_num] = d_false


def clear_maps():
    global distances_true, distances_false
    distances_true.clear()
    distances_false.clear()


def evaluate_condition(condition_num, op, lhs, rhs):
    k = 1
    if (op == "Eq"):
        newLhs = lhs if type(lhs) is int else ord(lhs)
        newRhs = rhs if type(rhs) is int else ord(rhs)
        diff = abs(newLhs - newRhs)
        distanceTrue = 0 if diff == 0 else diff
        distanceFalse = 0 if diff != 0 else k
    elif(op == "Ne"):
        newLhs = lhs if type(lhs) is int else ord(lhs)
        newRhs = rhs if type(rhs) is int else ord(rhs)
        diff = abs(newLhs - newRhs)
        distanceTrue = 0 if diff != 0 else k
        distanceFalse = 0 if diff == 0 else diff
    elif (op == "Le"):
        distanceTrue = 0 if (lhs <= rhs) else (lhs - rhs)
        distanceFalse = 0 if (lhs > rhs) else (rhs - lhs) + k
    elif (op == "Lt"):
        distanceTrue = 0 if (lhs < rhs) else (lhs - rhs) + k
        distanceFalse = 0 if (lhs >= rhs) else (rhs - lhs)
    elif (op == "Ge"):
        distanceTrue = 0 if (lhs >= rhs) else (rhs - lhs)
        distanceFalse = 0 if (lhs < rhs) else (lhs - rhs) + k
    elif (op == "Gt"):
        distanceTrue = 0 if (lhs > rhs) else (rhs - lhs) + k
        distanceFalse = 0 if (lhs <= rhs) else (lhs - rhs)
    elif (op == "In"):
        distanceTrue = sys.maxsize
        distanceFalse = 0
        rhs = list(rhs.keys()) if type(rhs) is dict else rhs
        for i in range(0, len(rhs)):
            newLhs = lhs if type(lhs) is int else ord(lhs)
            newRhs = rhs[i] if type(rhs[i]) is int else ord(rhs[i])
            if newLhs == newRhs:
                distanceTrue = 0
                distanceFalse = 1
                break
            else:
                diff = abs(newLhs - newRhs)
                distanceTrue = min(distanceTrue, diff)
                distanceFalse = 0
    else:
        raise ValueError("Invalid condition")
    result = (distanceTrue == 0)
    update_maps(condition_num, distanceTrue, distanceFalse)
    return result
