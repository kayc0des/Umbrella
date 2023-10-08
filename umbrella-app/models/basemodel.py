import uuid
import datetime
from engine.file_storage import FileStorage

storage = FileStorage()

class BaseModel():
    """BaseModel Class for all umbrella Data Models"""

    def __init__(self, **kwargs):
        """Constructor method called when an instance of the BaseModel is created"""
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def save(self):
        # Updates the created at time
        key = f"{self.__class__.__name__}.{self.id}"
        storage.new(key, self.to_dict())
        storage.save()
        self.updated_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        # for debugging
        return (f"[{self.__class__.__name__}] ({self.id}) {self.created_at}")

    def to_dict(self):
        bm_dict = self.__dict__
        bm_dict['id'] = str(self.id)
        bm_dict['__class__'] = self.__class__.__name__
        return bm_dict
    
    def from_dict(self):
        
        pass
    
# Debug
model = BaseModel(name='test', use='debug')
model.save()

model2 = BaseModel(name='test2', use='debug')
check1 = model2.save()

check2 = storage.reload()
print(check1 == check2)