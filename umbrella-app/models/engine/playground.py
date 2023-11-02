import json

with open("storage.json", "r") as json_file:
    data =  json.load(json_file)
    print(type(data))

def myFunc(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} has a value of {value}")
    
    if 'name' in kwargs:
        print("name found")

myFunc(name="John", age=18, sex="male")