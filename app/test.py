import requests

url='http://localhost/create/abcd'

payload={}
headers={}

for i in range(0,500):
    response = requests.request('GET', url, headers=headers, data=payload)