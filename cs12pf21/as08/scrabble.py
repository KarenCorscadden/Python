#!/usr/bin/env python3
"""
You shall write a Python program that:

Reads an arbitrary number of whitespace-delimited words from standard input.
Determines and prints (to standard output) two integer values:
The number of input words that are valid Scrabble words (case-insensitive), i.e. those that can be
found in /srv/datasets/scrabble-hybrid.
The total number of points that all those words would be worth in Scrabble, according to the letter
values in /srv/datasets/scrabble-letter-values.
"""

import sys

# add all scrabble dictionary words to a set
dictionary = {line.strip() for line in open('/srv/datasets/scrabble-hybrid')}

# add all letter/points value pairs to a dictionary
scrabble_values = dict()
with open('/srv/datasets/scrabble-letter-values') as value_file:
    for line in value_file:
        letter, value = line.strip().split()
        scrabble_values[letter] = int(value)

# check if the words are in the dictionary, if so count them and count up the points
words = 0
points = 0
for input_line in sys.stdin:
    for input_word in input_line.upper().split():
        if input_word in dictionary:
            words += 1
            for input_letter in input_word:
                points += scrabble_values[input_letter]

print(f'{words} words worth {points} points')
