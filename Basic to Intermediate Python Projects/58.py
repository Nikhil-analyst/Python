#Add a new employee to the json file.

import json
from pprint import pprint
#
# with open("company1.json", "r+") as file:
#     d = json.loads(file.read())
#     d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
#     file.seek(0)
#     json.dump(d, file, indent=4, sort_keys=True)
#     file.truncate()

entry = {"firstName" : "Jack", "lastName" : "Petter"}
with open("company1.json","r+") as file:
    d = json.load(file)
    d["employees"].append(entry)
    # file.seek(0)
    # json.dump(d, file)
    # file.truncate()
    pprint((d))