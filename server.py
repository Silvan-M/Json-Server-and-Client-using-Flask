import simplejson as json
from flask import Flask
app = Flask(__name__)

table = ["String",("Fabian","Timothy"),{"Name":"Atomic Bomb","Aerosol":True,"Explosive":True}]
data = json.dumps(table)

@app.route('/')
def hello_world():
    return data