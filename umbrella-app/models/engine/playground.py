import json

with open("storage.json", "r") as json_file:
    data =  json.load(json_file)
    print(type(data))