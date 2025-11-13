from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import book_author
from repositories.book_author import BookAuthorQuery

router = APIRouter(prefix="/book-authors", tags=["BookAuthors"])

@router.post("/", response_model=book_author.BookAuthor)
def create_book_author(ba: book_author.BookAuthorCreate, db: Session = Depends(get_db)):
    return BookAuthorQuery.create_book_author_query(ba, db)

@router.get("/", response_model=list[book_author.BookAuthor])
def list_book_authors(db: Session = Depends(get_db)):
    return BookAuthorQuery.list_book_authors_query(db)

@router.get("/{book_id}/{author_id}", response_model=book_author.BookAuthor)
def get_book_author(book_id: str, author_id: str, db: Session = Depends(get_db)):
    ba = BookAuthorQuery.get_book_author_query(book_id, author_id, db)
    if not ba:
        raise HTTPException(status_code=404, detail="BookAuthor not found")
    return ba

@router.delete("/{book_id}/{author_id}")
def delete_book_author(book_id: str, author_id: str, db: Session = Depends(get_db)):
    return BookAuthorQuery.delete_book_author_query(book_id, author_id, db)

