from basemodel import User, Message
from sqlalchemy.orm import Session
from connect import engine

session = Session(bind=engine)

user1 = User(
    username = "John Weigl",
    email = "john.w@gmail.com",
    # messages = [
    #     Message(text="Hi Umbrella"),
    #     Message(text="Please Subscribe"),
    # ]
)

paul = User(
    username = "Paul Wayne",
    email = "wayne@gmail.com",
    # messages = [
    #     Message(text="What's Up?"),
    #     Message(text="Right here!"),
    # ]
)

session.add_all([user1, paul])

#commit changes to database
session.commit()
