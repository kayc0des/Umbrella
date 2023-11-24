from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text, String
from typing import List


class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(length=50), nullable=False)
    email:Mapped[str] = mapped_column(String(length=255), nullable=False)
    message:Mapped[List["Message"]] = relationship(back_populates='user')

    def __repr__(self) -> str:
        return f"<User username={self.username}>"


class Message(Base):

    __tablename__ = 'messages'
    
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    text:Mapped[str] = mapped_column(Text, nullable=False)
    user:Mapped["User"] = relationship(back_populates='messages')

    def __repr__(self) -> str:
        return f"<comment text={self.text} by {self.user.username}>"