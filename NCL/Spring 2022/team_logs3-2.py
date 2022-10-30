import base64
import pickle

with open("oddball.log") as efile:
  for encoded in efile:
    line_bytes = base64.b64decode(encoded)
    data = pickle.loads(line_bytes)
    print(data)