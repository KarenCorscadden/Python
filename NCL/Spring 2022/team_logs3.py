import base64
import datetime
from struct import Struct

'''with open("oddball.log") as efile:
  with open("team_logs3-nonewlines.out", "wb") as dfile:
    for encoded in efile:
      print(len(encoded))
      decoded = base64.b64decode(encoded)
      dfile.write(decoded)
'''

'''
HEAD[0..1] - Always 1034
HEAD[2..5] - IP
HEAD[6] - Always 16
HEAD[7] - Request type! 0 = get, 1 = post, 2 = head (for sure)
HEAD[8] - Always 24
HEAD[9..] - Size - encoded in reverse order, high bit set indicates more data
HEAD - ends with 34decimal

One byte for len(path)
path

mid[0] - Always 40
mid[1] - Several values: 148, 173, 176, 206
mid[2] - Several values: 1, 2, 3
mid[3] - Always 50

One byte for len(user_agent)
user_agent

tail[0] unknown, values: 45, 46, 48, 49, 50, 52, 53, 54, 55, 56, 57, 85, 99, 100, 101, 105, 109, 110, 111, 116
tail[1..4] timestamp
tail[5] always 6, timezone?
'''

head_struct = Struct("HBBBBBBBBBBBB")
mid_struct = Struct("BBBBB")
tail_struct = Struct("BIB")

date_transfers = {}

with open("oddball.log") as efile:
  for encoded in efile:
    line_bytes = base64.b64decode(encoded)
    head_bytes = line_bytes[0:line_bytes.find(34, 6)+2]
    head = head_struct.unpack(line_bytes[:head_struct.size])
    tail = tail_struct.unpack(line_bytes[-tail_struct.size:])

    size_bytes = head_bytes[9:head_bytes.find(34, 6)]
    size_bytes = size_bytes[::-1]
    size = 0
    for size_byte in size_bytes:
      size = size << 7
      size += int(size_byte & 0x7f)

    ''' path '''
    next = line_bytes[len(head_bytes):]
    path_length = next.find(ord('('))
    path = next[:path_length]

    #print(f"{size} {path}")

    ''' middle structure'''
    next = next[path_length:]
    mid = mid_struct.unpack(next[:mid_struct.size])

    epoch = tail[1]
    date = datetime.datetime.fromtimestamp(epoch).date()

    if date not in date_transfers:
        date_transfers[date] = 0
    date_transfers[date]+=size
    
    next = next[mid_struct.size:]
    user_agent = next[:len(next)-tail_struct.size]

    #print(f"{tail}")
    #print(f"{mid} {len(user_agent)} {path} {user_agent}")
    #print(f"{head[6]}, {head[8:]} {path}")
    #print(f"{len(path)} {path} {user_agent}")
    #print (f"{str(mid)} {str(tail)}")
    #print(str(user_agent))
    #print(f"{head[0]} {'.'.join(map(str,head[1:5]))} - {' '.join(map(str,head[5:]))} - {' '.join(map(str,tail))}{str(path)}")

for day in date_transfers.items():
  print(f"{day[0]} - {day[1]}")