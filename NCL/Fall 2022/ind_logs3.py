entries = []
with open("minimal.hex.log") as file:
  for line in file:
    entries.append(int(line, 16))

#print(entries)
mask3 = 0b111
mask2 = 0b11
value_of_func_3 = {}
entries_of_id_3 = 0
num_values_func_2 = 0
sum_values_func_2 = 0
for entry in entries:
  v = mask3 & entry
  entry = entry >> 3
  f = mask2 & entry
  entry = entry >> 2
  i = mask3 & entry
  if int(f) == 3:
    if not int(v) in value_of_func_3:
      value_of_func_3[int(v)] = 1
    else:
      value_of_func_3[int(v)] += 1
  if int(i) == 3:
    entries_of_id_3 += 1
  if int(f) == 2:
    num_values_func_2 += 1
    sum_values_func_2 += int(v)

print(value_of_func_3)
print(entries_of_id_3)
print(sum_values_func_2/num_values_func_2)
