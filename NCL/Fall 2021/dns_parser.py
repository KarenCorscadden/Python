# set_dns = {(line.split()[4], line.split()[0]) for line in open('dig_out')}
starting_strings = {"0.", "10.", "127.", "169.254.", "192.0.0.", "192.0.2.", "192.88.99.", "192.168.",
                    "198.168.", "198.18.", "198.19.", "198.51.100.", "203.0.113.", "233.252.0."}
sunk = []

with open('dig_out') as dig_file:
    for line in dig_file:
        try:
            dns = (line.split()[4], line.split()[0])
            ip = []
            for string in starting_strings:
                if dns[0].startswith(string):
                    sunk.append(line)
                    break
            if dns[0] not in sunk:
                try:
                    ip = [int(dns[0].split(".")[0]), int(dns[0].split(".")[1]), int(dns[0].split(".")[2]), int(dns[0].split(".")[3])]
                except ValueError:
                    continue
                if ip[0] == 100 and ip[1] >= 64 and ip[1] <= 127:
                    sunk.append(line)
                elif ip[0] == 172 and ip[1] >= 16 and ip[1] <= 31:
                    sunk.append(line)
                elif ip[0] >= 224 and ip[0] <= 239:
                    sunk.append(line)
                elif ip[0] >= 240 and ip[0] <= 255:
                    sunk.append(line)
                elif ip[3] == 255 or ip[3] == 0:
                    sunk.append(line)

        except IndexError:
            print(f'IndexError: {line}')
            continue
print(f'Sunk: length {len(sunk)}: ')
for item in sunk:
    print(item, end='')
