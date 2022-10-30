import urllib.request, urllib.error, urllib.parse

while True:
  with urllib.request.urlopen('https://bulldoghax.com/secret/spinner') as response:
  #response = urllib.request.urlopen("https://bulldoghax.com/secret/spinner")
    html = response.read().decode().split("\n")
    html = html[14][24:34]
    print(html)
    cookies_dict = {"Cookie":"timelock=" + html}
    req = urllib.request.Request('https://bulldoghax.com/secret/codes', headers=cookies_dict)
    with urllib.request.urlopen(req) as response2:
      the_page=response2.read()
      print(the_page)
  