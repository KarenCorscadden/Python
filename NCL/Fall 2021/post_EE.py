#!/usr/bin/env python3

import hashlib
import subprocess

prefix = ["NCL-S", "SKY-S"]
eight = "-"
eleven = "9"
"""
for p in prefix:
    for l1 in range(65,91):
        for l2 in range(65,91):
            for l3 in range(65,91):
                for d1 in range(10):
                    for d2 in range(10):
                        for d3 in range(10):
                            x = p + chr(l1) + chr(l2) + chr(l3) + "-" + str(d1) + str(d2) + "9" + str(d3)
"""
# hash = hashlib.md5(x.encode("utf-8")).hexdigest()
x = "SKY-SIFT-8391\n"
z = ""
print(x)
for y in range(13):
    z = z + str(hex(ord(x[y])))[2:]
print('input to bytes:')
print(z)
# print(z[:16])
# print(str(hash)[:16])
# if z[:16] == str(hash)[:16]:
#    print("Correct answer!!!!")
#    print(x)
b_not = bytes(x, 'utf-8')
print('b_not:')
print(b_not)
b = bytes(z, 'utf-8')
print("bytes:")
print(b)

process = subprocess.Popen(['rock'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
process.stdin.write(b_not)
process.stdin.close()
process.wait()
#print(process.stdout.read())
if "Wrong" not in str(process.stdout.read()):
    print("Correct answer follows!!!!!!")
    print(x)
    quit()

print("No match found.")
