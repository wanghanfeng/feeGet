import requests

url = "http://202.97.210.38:9002/usr_cardb_main.ktcl"

response = requests.request("GET",url)

print(response.text)
