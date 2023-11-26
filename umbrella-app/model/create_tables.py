from basemodel import Base, User, Message
from connect import engine

print("CREATING TABLES >>>>> ")
Base.metadata.create_all(bind=engine)