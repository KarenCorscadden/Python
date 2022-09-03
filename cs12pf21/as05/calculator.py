#!/usr/bin/env python3

"""
A Python program that behaves as a simple calculator by processing input commands.
Each command shall consist of one line on standard input, and shall be closely analogous to
pressing a button (or buttons) on a classic digital calculator.

All numeric values shall be considered floats. The calculator shall begin with a result of 0 and
shall process commands until no more input is available. When input is exhausted, the program shall
print one line to standard output indicating the final result of the calculations, then quit.

Valid operators include +, -, *, /, ^, c

c shall behave like a clear button.
"""

left = 0
right = 0
operand = ""
command = ""
i = True
while i:
    try:
        command = input()
        if command == "+" or command == "-" or command == "*" or command == "/" or command == "^" \
            or command == "%":
            operand = command
        elif command == "c":
            left = 0
            right = 0
            operand = ""
        else:
            try:
                if operand == "":
                    left = float(command)
                else:
                    right = float(command)
                    if operand == "+":
                        left += right
                    elif operand == "-":
                        left -= right
                    elif operand == "*":
                        left *= right
                    elif operand == "/":
                        left = left / right
                    elif operand == "^":
                        left = left ** right
                    elif operand == "%":
                        left = left % right
                    operand = ""

            except ValueError:
                continue

    except (EOFError, KeyboardInterrupt):
        i = False

print(left)
