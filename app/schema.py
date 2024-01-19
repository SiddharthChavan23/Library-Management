from pydantic import BaseModel
from typing import Optional
from datetime import datetime
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


class UserDependency(BaseModel):
    user_id: int
    user_name: str
    email: str
class UserDependencyPut(BaseModel):
    user_name: Optional[str] = None
    email: Optional[str] = None



class CheckedOutUsers(BaseModel):
  id: int
  book_id: int
  user_id: int
  checkout_date: datetime
  return_date: datetime = None