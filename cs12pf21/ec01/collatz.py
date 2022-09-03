#!/usr/bin/env python3

"""
reads (without a prompt) a positive integer from standard standard input
prints the Collatz sequence starting at that number (and ending at 1)
"""

# Read 1 line of standard input. Converts to number of cents.
collatz = int(input())

while collatz != 1:
    print(collatz, end=", ")
    if collatz % 2 == 0:
        collatz = collatz // 2
    else:
        collatz = (collatz * 3) + 1

print(collatz)
