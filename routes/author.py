from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import author
from repositories.author import AuthorQuery

router = APIRouter(prefix="/authors", tags=["Authors"])

@router.post("/", response_model=author.Author)
def create_author(author: author.AuthorCreate, db: Session = Depends(get_db)):
    return AuthorQuery.create_author_query(author, db)

@router.get("/", response_model=list[author.Author])
def list_authors(db: Session = Depends(get_db)):
    return AuthorQuery.list_authors_query(db)

@router.get("/{author_id}", response_model=author.Author)
def get_author(author_id: str, db: Session = Depends(get_db)):
    author = AuthorQuery.get_author_query(author_id, db)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.put("/{author_id}", response_model=author.Author)
def update_author(author_id: str, author: author.AuthorUpdate, db: Session = Depends(get_db)):
    updated = AuthorQuery.update_author_query(author_id, author, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated

@router.delete("/{author_id}")
def delete_author(author_id: str, db: Session = Depends(get_db)):
    deleted = AuthorQuery.delete_author_query(author_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Author not found")
    return deleted
