infile = "output.txt"
outfile = "binaryoutput.txt"
with open(infile, "rb") as input:
  with open(outfile, "wb") as output:
    for line in input:
      for char in line:
        if (ord(char) < 20 or ord(char) > 126) and ord(char) != 10 and ord(char) != 13:
          output.write(line)
          break