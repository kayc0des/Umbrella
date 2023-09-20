import json

class FileStorage():
    """Serializes instances to JSON and deserializes JSON to instances"""

    __file_path = 'storage.json'
    __objects = dict()

    def all(self):
        # returns the dictionary object
        return self.__objects

    def new(self, obj):
        # Sets in __objects the obj with key <obj class name>.id
        key = f"{obj.__class__.__name__}.{obj['id']}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file, indent=4)

    def reload(self):
        pass

storage = FileStorage()

#debug
class dataSet():

    def __init__(self):
        self.id = 99
        self.name = 'test'
        self.year = 2023
        self.speciality = 'Software Engineering'

    def to_dict(self):
        return self.__dict__
    
    def save(self):
        storage.new(self.to_dict())
        storage.save()


randomData = dataSet()
randomData.save()
