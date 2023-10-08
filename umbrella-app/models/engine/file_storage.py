import json

class FileStorage():
    """Serializes instances to JSON and deserializes JSON to instances"""

    __file_path = 'storage.json'
    __objects = dict()

    def all(self):
        # returns the dictionary object
        return self.__objects

    def new(self, key, obj):
        # Sets in __objects the obj with key <obj class name>.id
        self.__objects[key] = obj

    def save(self):
        """Convert object into JSON"""
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file, indent=4)

    def reload(self):
        """Convert JSON to object"""
        try:
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
                print(f"After reload we have {self.__objects}")
        except Exception as error:
            print(f"Error: {error}")