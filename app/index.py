from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models import Book,User,CheckedOutUser
from app.db import Base, SessionLocal, engine
from app.schema import BookCreate, BookUpdate, Bookall, UserDependency,UserDependencyPut
from datetime import datetime


Base.metadata.create_all(bind=engine)
app = FastAPI()
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/books', response_model=list[Bookall])
async def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books

@app.post("/books/create")
async def create_book(books_create: List[BookCreate], db: Session = Depends(get_db)):
    try:
        for book_data in books_create:
            new_book = Book(**book_data.dict())
            db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return {"message": "Books created successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating book: {e}")
    finally:
        db.close()

@app.put("/books/update/{book_id}")
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    try:
        existing_book = db.query(Book).filter(Book.id == book_id).first()

        if existing_book is None:
            raise HTTPException(status_code=404, detail="Book not found")

        for field, value in book_update.dict(exclude_unset=True).items():
            setattr(existing_book, field, value)

        db.commit()
        db.refresh(existing_book)
        return existing_book
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating book: {e}")
    finally:
        db.close()
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return {"message": "Book deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")
    





@app.get('/user', response_model=list[UserDependency])
async def get_user(db: Session = Depends(get_db)):
    user = db.query(User).all()
    return user

@app.put("/users/{user_id}")
async def update_user(user_id: int, user_data: UserDependencyPut):
    user = next((u for u in get_db if u['user_id'] == user_id), None)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Update only the provided fields
    for field, value in user_data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    return user
@app.post("/users/create")
async def create_user(user: List[UserDependencyPut],db: Session=Depends(get_db)):
    try:
        for user in user:
            new_user = User(**user.dict())
            db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating book: {e}")
    finally:
        db.close()

@app.get("/checkout/")
def read_checkout(db: Session = Depends(get_db)):
  checkout = db.query(CheckedOutUser).all()
  return checkout
@app.post("/checkout/")
def check_out_book(book_id: int, user_id: int, db: Session = Depends(get_db)):
   book_avail = db.query(Book).filter(Book.id == book_id, Book.is_checked_out == 0).first()
   if not book_avail:
        raise HTTPException(status_code=400, detail="Book is not available for checkout")
   book_avail.is_checked_out = 1

   new_checkout = CheckedOutUser(
       book_id=book_id, 
       user_id=user_id,
       checkout_date = datetime.now()
   )
   db.add(new_checkout)
   db.commit()
   return "Successfull checkout"
@app.put("/return/")
def return_book(checkout_id: int, db: Session = Depends(get_db)):
   checkout = db.query(CheckedOutUser).filter(CheckedOutUser.id == checkout_id).first()
   if not checkout:
        raise HTTPException(status_code=400, detail="Checkout record not found")
   checkout.return_date = datetime.now() 
   book = checkout.book
   book.is_checked_out = 0
   db.commit()
   return f"Book has been successfully returned on {datetime.now()} "



@app.get("/generate_report/")
def generate_report(db: Session = Depends(get_db)):
    # Fetch checked-out books data
    checked_out_books = (
        db.query(CheckedOutUser, Book, User)
        .join(Book, CheckedOutUser.book_id == Book.id)
        .join(User, CheckedOutUser.user_id == User.user_id)
        .all()
    )

    # Format the data into a report
    report = []
    for checkout, book, user in checked_out_books:
        report_entry = {
            "checkout_id": checkout.id,
            "book_title": book.title,
            "user_name": user.user_name,
            "checkout_date": checkout.checkout_date,
            "return_date": checkout.return_date,
        }
        report.append(report_entry)

    return report