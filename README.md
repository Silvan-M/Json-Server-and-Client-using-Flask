# What does it do?
This is the most simple way of running a JSON flask server, hosting a json file and parsing it afterwards.
It takes as input the `table` variable and hosts it as json on localhost with port 5000, then the client can read this json and converts it to a pyhton table.

# Install
Commands for modules:
- pip install flask
- pip install simplejson

# Run the server
CMD:
- cd into the python directory
- run `export FLASK_APP=server.py`
- run `python -m flask run`
- Access the server at "http://localhost:5000/"

# Client 
Simply run the `client.py` python script.
