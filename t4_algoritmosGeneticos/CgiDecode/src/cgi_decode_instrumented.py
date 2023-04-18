from src.evaluate_condition import evaluate_condition
def cgi_decode_instrumented(test_case):
    """Decode the CGI-encoded string `test_case`:
       * replace "+" by " "
       * replace "%xx" by the character with hex number xx.
       Return the decoded string.  Raise `ValueError` for invalid inputs."""

    # Mapping of hex digits to their integer values
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }

    t = ""
    i = 0
    while evaluate_condition(1, 'Lt', i, len(test_case)):  # c1
        c = test_case[i]
        if evaluate_condition(2, 'Eq', c, '+'):  # c2
            t += ' '
        elif evaluate_condition(3, 'Eq', c, '%'):  # c3
            digit_high, digit_low = test_case[i + 1], test_case[i + 2]
            i += 2
            if evaluate_condition(4, 'In', digit_high, hex_values) and evaluate_condition(5, 'In', digit_low, hex_values):  # c4 and c5
                v = hex_values[digit_high] * 16 + hex_values[digit_low]
                t += chr(v)
            else:
                raise ValueError("Invalid encoding")
        else:
            t += c
        i += 1
    return t
