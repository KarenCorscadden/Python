"""
This module contains functions defined as practice in defining and calling functions.
"""

__author__ = 'Karen Corscadden, a Cabrillo student for CS 12P, kmcorscadden@jeff.cis.cabrillo.edu'

import re  # For splitting lines from file syllables.txt. Do not use other library modules.


def _load_data():
    """
    Loads data from files. For internal use only, i.e. "private".
    You don't *have* to structure things this way, but it's a recommendation.
    """
    dict_ud = {line.split()[0]: line.split()[1]
                for line in open('/srv/datasets/unicode-upside-down')}
    dict_syllables = dict()
    for line in open('/srv/datasets/syllables.txt'):
        line = line.rstrip()
        s = re.split(r'[;\-]', line)
        word = ''
        for x in s:
            word = word + x
        dict_syllables[word] = s
    return dict_ud, dict_syllables


_to_upside_down, _syllables = _load_data()  # Use our "private" function to load required file data.


def babylonian_sqrt(square, iterations=None):
    """
    Computes the square root of a numeric value (assumed to be positive) via the Babylonian method.
    Uses an initial guess as described at the URL below.
    If iterations is a positive integer, the process stops after that many guesses.
    Otherwise, the process stops when the a new guess equals the previous guess.
    See: https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html
    """
    # Sanity checks. Feel free to remove these:
    assert iterations is None or isinstance(iterations, int) and iterations > 0
    assert isinstance(square, (int, float)) and square > 0
    x_one = 0.0
    # make initial guess
    if len(str(int(square))) % 2 == 0:
        x_not = len(str(int(square))) // 2
    else:
        x_not = (len(str(int(square))) + 1) // 2
    two_guess = float('2' + '0' * (x_not - 1))  # float(2 * 10 ** (x_not - 1))
    seven_guess = float('7' + '0' * (x_not - 1))
    if abs(two_guess * two_guess - square) < abs(seven_guess * seven_guess - square):
        x_not = two_guess
    else:
        x_not = seven_guess
    if iterations is None:
        x_one = (x_not + square / x_not) / 2
        while x_not != x_one:
            x_not = x_one
            x_one = (x_not + square / x_not) / 2
        return x_not
    elif iterations == 1:
        return x_not
    else:
        for _ in range(2, iterations + 1):
            x_one = (x_not + square / x_not) / 2
            x_not = x_one
        return x_not


def hailstone_sequence(number):
    """
    Returns a list containing the sequence of hailstone numbers starting at a given number.
    The number is assumed to be a positive integer.
    See: https://mathworld.wolfram.com/HailstoneNumber.html
    """
    assert isinstance(number, int) and number > 0  # Sanity check. Feel free to remove this.
    collatz = []
    while number != 1:
        collatz.append(number)
        if number % 2 == 0:
            number = number // 2
        else:
            number = (number * 3) + 1
    collatz.append(number)
    return collatz


def syllables(word):
    """
    Returns a tuple containing the lowercase syllables of a case-insensitive word, according to
    file /srv/datasets/syllables.txt. If a word is not present in the dataset, this returns a
    single-element tuple containing only the lowercase word itself.

    This function should not read from the syllables.txt file, but rather use an object containing
    the relevant file data that was populated upon loading the module.
    """
    assert isinstance(word, str)  # Sanity check. Feel free to remove this.
    stripped = re.sub(r'[;\-]', '', word)
    try:
        s = tuple(_syllables[stripped.lower()])
        return s
    except KeyError:
        return (word.lower(), )


def upside_down(text):
    """
    Returns the "upside down" representation of a string assumed to contain "English" text, i.e. the
    text in reverse with all relevant characters replaced by their "upside-down" versions, according
    to file /srv/datasets/unicode-upside-down.

    This function should not read from the unicode-upside-down file, but rather use an object
    containing the relevant file data that was populated upon loading the module.
    """
    assert isinstance(text, str)  # Sanity check. Feel free to remove this.
    ud = ''
    if len(text) > 0:
        for c in text:
            try:
                ud += _to_upside_down[c]
            except KeyError:
                ud += c
    return ud[::-1]


if __name__ == '__main__':
    # Note the expected return values in these assertion-based tests.
    # See: https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement
    assert babylonian_sqrt(16) == 4
    assert babylonian_sqrt(16, iterations=1) == 2
    assert babylonian_sqrt(16, iterations=2) == 5
    assert babylonian_sqrt(16, iterations=3) == 4.1
    assert babylonian_sqrt(1e100) == 1e50
    assert hailstone_sequence(1) == [1]
    assert hailstone_sequence(2) == [2, 1]
    assert hailstone_sequence(3) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert hailstone_sequence(4) == [4, 2, 1]
    assert hailstone_sequence(5) == [5, 16, 8, 4, 2, 1]
    assert hailstone_sequence(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert syllables('Hello') == ('hel', 'lo')
    assert syllables('pandemonium') == ('pan', 'de', 'mo', 'ni', 'um')
    assert syllables('self-righteously') == ('self', 'right', 'eous', 'ly')
    assert syllables('Instagram') == ('instagram',)
    assert upside_down('Hello!') == '¡ollǝH'
    assert upside_down('') == ''
    assert upside_down(
      'Well, well, well. How the turntables...') == "˙˙˙sǝlqɐʇuɹnʇ ǝɥʇ ʍoH ˙llǝʍ 'llǝʍ 'llǝM"
    # If this module is the main module, we print the "upside down" version of text in standard
    # input.
    # import sys
    # print(upside_down(sys.stdin.read().rstrip('\n')))
