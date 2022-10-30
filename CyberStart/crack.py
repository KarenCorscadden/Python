import requests

one = requests.get('https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D', verify=False)
two = requests.get('https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D', verify=False)
three = requests.get('https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D', verify=False)
four = requests.get('https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D', verify=False)
five = requests.get('https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D', verify=False)
key = one.content + two.content + three.content + four.content + five.content
print(key)
ans_url = 'https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string=' + key
print(ans_url)
answer = requests.get(ans_url, verify=False)
print(answer.content)