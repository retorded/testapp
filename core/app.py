def sumtwoints(a, b):
    # typecheck
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("Input not ints")


def multiplytwoints(a, b):
    return a * b
