import requests

res = requests.get('http://vnexpress.net')

print(res.text)
