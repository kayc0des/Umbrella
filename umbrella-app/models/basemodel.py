import uuid
import datetime
from engine.file_storage import FileStorage

storage = FileStorage()

class BaseModel():
    """BaseModel Class for all umbrella Data Models"""

    def __init__(self, **kwargs):
        """Constructor method called when an instance of the BaseModel is created"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = self.created_at
        else:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            # else:
            #     kwargs['created_at'] = datetime.datetime.strftime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            # else:
            #     kwargs['updated_at'] = datetime.datetime.strftime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            
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
        bm_dict['id'] = self.id
        bm_dict['__class__'] = self.__class__.__name__
        return bm_dict
    
    def from_dict(self):
        
        pass
    
# Debug
model = BaseModel(id = '12fcb22b-4221-4802-932a-ed486d4271e0', created_at = '2023-10-08T12:43:56.460601', updated_at = '2023-10-08T12:43:56.460601', name = 'test2', use = 'debug', __class__ = 'BaseModel')
model.save()
