import requests
import simplejson as json

response = requests.get("http://localhost:5000/")
data = response.content
table = json.loads(data)

print("The name of the masters of the aerosol is {} and {}.".format(table[1][0],table[1][1]))