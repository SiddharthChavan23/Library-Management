from sqlalchemy.sql.expression import null
from app.db import Base
from sqlalchemy import String,Integer,Column,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    author = Column(String(100))
    published_year = Column(Integer)
    is_checked_out = Column(Integer, default=0)
    checked_out_users = relationship("CheckedOutUser", back_populates="book")

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), index=True)
    email = Column(String(100), index=True)

class CheckedOutUser(Base):
  __tablename__ = "checked_out_users"

  id = Column(Integer, primary_key=True)
  book_id = Column(Integer, ForeignKey("books.id"))
  user_id = Column(Integer, ForeignKey("user.user_id"))
  checkout_date = Column(DateTime)
  return_date = Column(DateTime,nullable=True)
  book = relationship("Book", back_populates="checked_out_users")