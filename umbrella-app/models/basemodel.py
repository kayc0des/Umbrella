import uuid
import datetime

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
        self.updated_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        # for debugging
        return (f"[{self.__class__.__name__}] ({self.id}) {self.created_at}")

    def to_dict(self):
        bm_dict = self.__dict__
        bm_dict[__class__] = self.__class__.__name__
    
# Debug
model = BaseModel()
model.to_dict()