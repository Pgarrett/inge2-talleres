from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import distances_true
from src.evaluate_condition import distances_false

def get_fitness_cgi_decode(test_suite):
    fitness = 0
    for test_case in test_suite:
        try:
            cgi_decode_instrumented(test_case)
        except Exception:
            pass
    for i in range(0, 5):
        if i in distances_true.keys():
            fitness += (distances_true[i]/(distances_true[i]+1))
            fitness += (distances_false[i]/(distances_false[i]+1))
        else:
            fitness += 1

    return fitness
