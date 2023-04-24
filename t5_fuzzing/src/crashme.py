import inspect
from fuzzingbook.MutationFuzzer import FunctionCoverageRunner


def crashme(s: str) -> None:
    if len(s) > 0 and s[0] == 'b':
        if len(s) > 1 and s[1] == 'a':
            if len(s) > 2 and s[2] == 'd':
                if len(s) > 3 and s[3] == '!':
                    raise Exception()


if __name__ == "__main__":
    input = "bad!"
    crashme_runner = FunctionCoverageRunner(crashme)

    lineas = len(inspect.getsourcelines(crashme)[0])
    print(f"El programa a correr tiene {lineas} lineas.")

    result, outcome = crashme_runner.run(input)
    print(f"El resultado de ejecutar crashme con el input {input} fue {result}")
    print(f"El outcome del Runner fue {outcome}")

    locations = crashme_runner.coverage()
    print(f"Las locations cubiertas durante la ejecución fueron:")
    for loc in locations:
        print(f" -> Función \"{loc[0]}\": línea {loc[1]}")