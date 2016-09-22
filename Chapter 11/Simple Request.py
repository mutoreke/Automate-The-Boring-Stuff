import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code == requests.codes.ok #Checks to see if request worked "protcol 200"
print(type(res))
print(len(res.text))
print(res.text[:250])

