def sumtwointegers(a, b):

    # typecheck
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise ValueError("Input not ints")

def multiplytwointegers(a, b):

    # typecheck
    if isinstance(a, int) and isinstance(b, int):
        return a*b
    else:
        raise ValueError("Input not ints")

def isaninteger(a):
    # typecheck
    if isinstance(a, int):
        return True
    else:
        return False
