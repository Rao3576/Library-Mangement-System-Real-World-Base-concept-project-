from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import borrowing
from repositories.borrowing_query import BorrowingQuery

router = APIRouter(prefix="/borrowings", tags=["Borrowings"])

@router.post("/", response_model=borrowing.Borrowing)
def create_borrowing(borrow: borrowing.BorrowingCreate, db: Session = Depends(get_db)):
    return BorrowingQuery.create_borrowing_query(borrow, db)

@router.get("/", response_model=list[borrowing.Borrowing])
def list_borrowings(db: Session = Depends(get_db)):
    return BorrowingQuery.list_borrowings_query(db)

@router.get("/{borrow_id}", response_model=borrowing.Borrowing)
def get_borrowing(borrow_id: str, db: Session = Depends(get_db)):
    b = BorrowingQuery.get_borrowing_query(borrow_id, db)
    if not b:
        raise HTTPException(status_code=404, detail="Borrowing not found")
    return b

@router.put("/{borrow_id}", response_model=borrowing.Borrowing)
def update_borrowing(borrow_id: str, borrow: borrowing.BorrowingUpdate, db: Session = Depends(get_db)):
    updated = BorrowingQuery.update_borrowing_query(borrow_id, borrow, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Borrowing not found")
    return updated

@router.delete("/{borrow_id}")
def delete_borrowing(borrow_id: str, db: Session = Depends(get_db)):
    return BorrowingQuery.delete_borrowing_query(borrow_id, db)
