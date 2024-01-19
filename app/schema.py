from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Pydantic model for displaying detailed information about a book

class Bookall(BaseModel):
    id :int
    title: str
    author: str
    published_year:int
    is_checked_out:int

    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int
    is_checked_out: int = 0

class BookUpdate(BaseModel):
    title: str = None
    author: str = None
    published_year: int = None
    is_checked_out: int = None


class BookDelete(BaseModel):
    id: int

# Pydantic model representing user information for dependency injection

class UserDependency(BaseModel):
    user_id: int
    user_name: str
    email: str
class UserDependencyPut(BaseModel):
    user_name: Optional[str] = None
    email: Optional[str] = None


# Pydantic model representing information about checked-out books and users

class CheckedOutUsers(BaseModel):
  id: int
  book_id: int
  user_id: int
  checkout_date: datetime
  return_date: datetime = None