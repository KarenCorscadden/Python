#!/usr/bin/env python3

"""
Consumes all text on standard input and determines:

The total number of lines in the text.
The total number of sentences in the text. A sentence shall be denoted by the presence of a period
(.), question mark (?) or exclamation mark (!) character at the end of a word.
The total number of words in the text. A word shall be considered any whitespace-delimited sequence
of characters.
The total number of English letters in the text, and the number of occurrences of each letter,
without regard to case.
The program shall print a summary of this data:
Line 1: The total number of lines in the text.
Line 2: The total number of sentences in the text.
Line 3: The total number of words in the text.
Line 4: The total number of English letters in the text.
Lines 5 - 30: Lines describing the number of occurrences and relative percentage frequency of each
letter, along with a simple visual histogram presented by printing a number of asterisks equivalent
to the letter's percentage of frequency rounded to the nearest integer.
"""
i = True
num_words = 0
num_lines = 0
num_sentences = 0
punctuation = (".", "!", "?")
char_list = [0] * 26

while i:
    try:
        line = input().split()
        num_lines += 1
        for word in line:
            num_words += 1
            if word[-1] in punctuation:
                num_sentences += 1
            for character in word.lower():
                if 0 <= ord(character) - ord("a") <= 25:
                    char_list[(ord(character) - ord("a"))] += 1

    except (EOFError, KeyboardInterrupt):
        i = False
num_letters = sum(char_list)
count_length = len(str(max(char_list)))

print(f"{num_lines} line{'s' if num_lines != 1 else ''}")
print(f"{num_sentences} sentence{'s' if num_sentences != 1 else ''}")
print(f"{num_words} word{'s' if num_words != 1 else ''}")
print(f"{num_letters} letter{'s' if num_letters != 1 else ''}")
for c in range(26):
    print(f"{chr(c + ord('a'))} {char_list[c]:>{count_length}} ", end="")
    print(f"{(char_list[c]/num_letters):>7.2%} {round(100 * char_list[c] / num_letters) * '*'}")
