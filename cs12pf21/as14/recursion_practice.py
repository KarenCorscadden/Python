"""
This module implements several functions in order to practice with recursion.
"""

import math  # We'll want this for square roots and assertions below


def fibonacci(i: int) -> int:
    """
    Recursively calculates index i of the Fibonacci sequence.
    See: https://en.wikipedia.org/wiki/Fibonacci_number

    :param i: an index in the Fibonacci sequence, assumed to be nonnegative
    :return: index i of the Fibonacci sequence
    """
    # We did this in class, so might as well just include the code here:
    if i < 2:
        return i
    return fibonacci(i - 1) + fibonacci(i - 2)


def most_precise(function):
    """
    Calls a function with successively larger positive integer arguments (starting from 1)
    until the function returns the same value twice in succession. Meant to work with
    functions like ρ and φ in this module, e.g. most_precise(ρ) will repeatedly call ρ
    requesting more levels of recursion until two successive calls return the same value.

    :param function: the function to call with successively larger arguments
    :return: the first repeated return value
    """
    n = 1
    x = function(n)
    y = function(n + 1)
    while x != y:
        x = y
        n += 1
        y = function(n + 1)
    return x


def padovan(i: int) -> int:
    """
    Recursively calculates index i of the Padovan sequence.
    See: https://en.wikipedia.org/wiki/Padovan_sequence

    :param i: an index in the Padovan sequence, assumed to be nonnegative
    :return: index i of the Padovan sequence
    """
    if i < 0:
        raise ValueError('Illegal input to function, must be a nonnegative integer.')
    elif i < 3:
        return 1
    return padovan(i - 2) + padovan(i - 3)


def perrin(i: int) -> int:
    """
    Recursively calculates index i of the Perrin sequence.
    See: https://en.wikipedia.org/wiki/Perrin_number

    :param i: an index in the Perrin sequence, assumed to be nonnegative
    :return: index i of the Perrin sequence
    """
    if i < 0:
        raise ValueError('Illegal input to function, must be a nonnegative integer.')
    elif i == 0:
        return 3
    elif i == 1:
        return 0
    elif i == 2:
        return 2
    return perrin(i - 2) + perrin(i - 3)


def ρ(levels: int) -> float:
    """
    Recursively calculates the plastic number (often denoted as the Greek letter "rho", i.e. ρ)
    via its nested radical representation.
    See: https://en.wikipedia.org/wiki/Plastic_number

    :param levels: the number of recursion levels, assumed to be nonnegative
    :return: ρ calculated via the requested number of recursive calls
    """
    if levels < 0:
        raise ValueError('Illegal input to function, must be a nonnegative integer.')
    elif levels == 0:
        return 1.0
    return (1.0 + ρ(levels - 1)) ** (1 / 3)


def φ(levels: int) -> float:
    """
    Recursively calculates the golden ratio (often denoted as the Greek letter "phi", i.e. ϕ or φ)
    via its nested radical representation.
    See: https://en.wikipedia.org/wiki/Golden_ratio

    :param levels: the number of recursion levels, assumed to be nonnegative
    :return: φ calculated via the requested number of recursive calls
    """
    if levels < 0:
        raise ValueError('Illegal input to function, must be a nonnegative integer.')
    elif levels == 0:
        return 1.0
    return math.sqrt(1.0 + φ(levels - 1))


if __name__ == '__main__':
    # test Fibonacci sequence
    assert list(fibonacci(i) for i in range(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    # test recursive φ
    assert φ(0) == math.sqrt(1)
    assert φ(1) == math.sqrt(1 + math.sqrt(1))
    assert φ(2) == math.sqrt(1 + math.sqrt(1 + math.sqrt(1)))
    assert φ(3) == math.sqrt(1 + math.sqrt(1 + math.sqrt(1 + math.sqrt(1))))
    most_precise_φ = most_precise(φ)
    assert most_precise_φ == φ(31)  # nested-radical φ should hit peak precision at 31 levels
    assert most_precise_φ == (1 + math.sqrt(5)) / 2  # closed-form solution should be equal
    # verify the relationship between Fibonacci sequence and φ (30 terms gets us within a billionth)
    assert abs(fibonacci(30) / fibonacci(29) - most_precise_φ) < 1e-9
    # test Padovan and Perrin sequences
    assert list(padovan(i) for i in range(10)) == [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    assert list(perrin(i) for i in range(10)) == [3, 0, 2, 3, 2, 5, 5, 7, 10, 12]
    # test recursive ρ
    assert ρ(0) == 1**(1 / 3)
    assert ρ(1) == (1 + 1**(1 / 3))**(1 / 3)
    assert ρ(2) == (1 + (1 + 1**(1 / 3))**(1 / 3))**(1 / 3)
    assert ρ(3) == (1 + (1 + (1 + 1**(1 / 3))**(1 / 3))**(1 / 3))**(1 / 3)
    most_precise_ρ = most_precise(ρ)
    assert most_precise_ρ == ρ(23)  # nested-radical ρ should hit peak precision at 23 levels
    assert most_precise_ρ == ((9 - math.sqrt(69)) / 18)**(1 / 3) + (
        (9 + math.sqrt(69)) / 18)**(1 / 3)  # closed-form solution should be equal
    # verify the relationship between the Padovan/Perrin sequences and ρ
    assert abs(padovan(52) / padovan(51) - most_precise_ρ) < 1e-9
    assert abs(perrin(52) / perrin(51) - most_precise_ρ) < 1e-9
