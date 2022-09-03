#!/usr/bin/env python3

"""
a solution to a modified version of Rosalind Problem GC that computes
the GC-content of a DNA string from standard input
"""

# Read the input (assume it's a DNA string)
dna = input()

# Calculate the GC-content
num_bases = dna.count("A") + dna.count("C") + dna.count("G") + dna.count("T")
gc_content = 0
if num_bases != 0:
    gc_content = (dna.count("G") + dna.count("C")) / num_bases

# Print GC-content rounded to three digits after the decimal
print("{:.3%} GC-content".format(gc_content))
