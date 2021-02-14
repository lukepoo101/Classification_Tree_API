import json

import requests

##Get new/up-to-date client code
client_code = json.loads(requests.get("https://classification-tree-api.herokuapp.com/update").content)

##write new code to file
with open("Client.py", "w") as client:
    client.write(client_code["update"])
