#!/usr/bin/env python3

"""
reads (without a prompt) a real number from standard input.
Assuming that value represents an amount in U.S. currency, the program shall then proceed to
print out how that amount could be represented using the fewest bills and coins, assuming that
only the following bills and coins exist:

$100 bills
$50 bills
$20 bills
$10 bills
$5 bills
$1 bills
Quarters ($0.25)
Dimes ($0.10)
Nickels ($0.05)
Pennies ($0.01)
"""

# Read 1 line of standard input. Converts to number of cents.
num_cur, num_cents = (0, int(round(float(input()) * 100)))

# Create dictionary to store output identifiers, index = number of cents
output_id = {
    10000: ('hundred', 'hundreds'),
    5000: ('fifty', 'fifties'),
    2000: ('twenty', 'twenties'),
    1000: ('ten', 'tens'),
    500: ('five', 'fives'),
    100: ('one', 'ones'),
    25: ('quarter', 'quarters'),
    10: ('dime', 'dimes'),
    5: ('nickel', 'nickels'),
    1: ('penny', 'pennies')
}

for x in output_id:
    num_cur, num_cents = divmod(num_cents, x)
    if num_cur > 0:
        print(f'{num_cur} {output_id[x][int(num_cur>1)]}')
