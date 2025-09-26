from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import bookstatus
from repositories.bookstatus_query import BookStatusQuery

router = APIRouter(prefix="/book-statuses", tags=["BookStatuses"])

@router.post("/", response_model=bookstatus.BookStatus)
def create_status(status: bookstatus.BookStatusCreate, db: Session = Depends(get_db)):
    return BookStatusQuery.create_status_query(status, db)

@router.get("/", response_model=list[bookstatus.BookStatus])
def list_statuses(db: Session = Depends(get_db)):
    return BookStatusQuery.list_statuses_query(db)

@router.get("/{status_id}", response_model=bookstatus.BookStatus)
def get_status(status_id: str, db: Session = Depends(get_db)):
    s = BookStatusQuery.get_status_query(status_id, db)
    if not s:
        raise HTTPException(status_code=404, detail="BookStatus not found")
    return s

@router.put("/{status_id}", response_model=bookstatus.BookStatus)
def update_status(status_id: str, status: bookstatus.BookStatusUpdate, db: Session = Depends(get_db)):
    updated = BookStatusQuery.update_status_query(status_id, status, db)
    if not updated:
        raise HTTPException(status_code=404, detail="BookStatus not found")
    return updated

@router.delete("/{status_id}")
def delete_status(status_id: str, db: Session = Depends(get_db)):
    return BookStatusQuery.delete_status_query(status_id, db)
