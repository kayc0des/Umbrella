import uuid
import datetime

class BaseModel():
    # Include all attributes and methods for all data objects

    def __init__(self):
        # Constructor method called when an instance of the BaseModel is created
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now().strftime("%c")

    def updated_at(self):
        self.created_at = datetime.datetime.now().strftime("%c")

    def __repr__(self):
        return (f"{self.__class__.__name__}: id: {self.id} timestamp: {self.created_at}")

    def to_dict(self):
        pass
    
# Test
model = BaseModel()
print(f"The unique identifier for model is: {model.id} and it was created at {model.created_at}")
print(model.__repr__())