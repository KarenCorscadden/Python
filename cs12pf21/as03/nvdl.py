#!/usr/bin/env python3

"""
reads four lines from standard input:

A person's first name
A person's middle name (o primer apellido, si es un nombre español)
A person's last name (o segundo apellido, si es un nombre español)
A person's pre-1998 Nevada driver license number
print three lines to standard output, namely:
The person's full name, formatted as follows. Ensure that the first letter of each name
component is capitalized, and the remaining letters are lowercase, i.e.:
Lastname, Firstname Middlename
The person's full Social Security number, with standard hyphenation, i.e.:
XXX-XX-XXXX
The person's age in years (as an integer value), comparing their birth date to the current date,
and assuming they were born on the first of January.
"""
import datetime
# Read 4 lines of standard input
f_name = input()
m_name = input()
l_name = input()
dl_num = input()

# Create full name formatted string and output it to standard output
full_name = l_name.capitalize() + ", " + f_name.capitalize() + " " + m_name.capitalize()
print(full_name)

# Calculate social security number and output it to standard output
# First ignore last two digits of DL Number
ssn = dl_num[:-2]
# convert ssn to integer
ssn = int(ssn)
# Then calculate the ssn and format to 9 characters filling with leading zeros
ssn = (ssn - 2600000001) / 2
ssn = f"{ssn:09.0f}"

# Output ssn formatted properly
print(f"{ssn[:3]}-{ssn[3:5]}-{ssn[5:]}")

# Calculate person's age in years and output to standard Output

birth_year = int(dl_num[-2:])
birth_year = birth_year + 1900
cur_date = datetime.datetime.now()
cur_year = cur_date.year
age = cur_year - birth_year
print(age)
