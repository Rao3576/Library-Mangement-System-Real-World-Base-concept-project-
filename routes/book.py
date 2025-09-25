from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import book
from repositories.book_query import BookQuery

router = APIRouter(prefix="/books", tags=["Books"])

@router.post("/", response_model=book.Book)
def create_book(book: book.BookCreate, db: Session = Depends(get_db)):
    return BookQuery.create_book_query(book, db)

@router.get("/", response_model=list[book.Book])
def list_books(db: Session = Depends(get_db)):
    return BookQuery.list_books_query(db)

@router.get("/{book_id}", response_model=book.Book)
def get_book(book_id: str, db: Session = Depends(get_db)):
    book = BookQuery.get_book_query(book_id, db)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=book.Book)
def update_book(book_id: str, book: book.BookUpdate, db: Session = Depends(get_db)):
    updated_book = BookQuery.update_book_query(book_id, book, db)
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}")
def delete_book(book_id: str, db: Session = Depends(get_db)):
    deleted = BookQuery.delete_book_query(book_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return deleted
