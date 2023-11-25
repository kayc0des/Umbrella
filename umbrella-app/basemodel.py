import uuid
import datetime
# from engine.file_storage import FileStorage
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, String
from typing import List


# storage = FileStorage()


class Base(DeclarativeBase):
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
            if 'updated_at' not in kwargs:
                kwargs['updated_at'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
            if '__class__' in kwargs:
                del kwargs['__class__']

            for key, value in kwargs.items():
                setattr(self, key, value)

    # def save(self):
    #     # Updates the created at time
    #     key = f"{self.__class__.__name__}.{self.id}"
    #     storage.new(key, self.to_dict())
    #     storage.save()
    #     self.updated_at = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    # def __str__(self):
    #     # for debugging
    #     return (f"[{self.__class__.__name__}] ({self.id}) {self.created_at}")

    # def to_dict(self):
    #     bm_dict = self.__dict__
    #     bm_dict['id'] = self.id
    #     bm_dict['__class__'] = self.__class__.__name__
    #     return bm_dict
    
    # def from_dict(self):
        
    #     pass


class User(Base):

    __tablename__ = 'users'

    id:Mapped[str] = mapped_column(String(length=50), primary_key=True)
    username:Mapped[str] = mapped_column(String(length=50), nullable=False)
    email:Mapped[str] = mapped_column(String(length=255), nullable=False)
    message:Mapped[List["Message"]] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f"<User username={self.username}>"


class Message(Base):

    __tablename__ = 'messages'
    
    id:Mapped[str] = mapped_column(String(length=50), primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    text:Mapped[str] = mapped_column(Text, nullable=False)
    user:Mapped["User"] = relationship(back_populates='message')

    def __repr__(self) -> str:
        return f"<comment text={self.text} by {self.user.username}>"
    

# Debug
# model = BaseModel(id = '12fcb22b-4221-4802-932a-ed486d4271e0', created_at = '2023-10-08T12:43:56.460601', updated_at = '2023-10-08T12:43:56.460601', name = 'test2', use = 'debug', __class__ = 'BaseModel')
# model.save()

# kayModel = BaseModel()
# kayModel.save()

# Debug
# if __name__ == "__main__":
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     model = BaseModel()
#     model.save(session)