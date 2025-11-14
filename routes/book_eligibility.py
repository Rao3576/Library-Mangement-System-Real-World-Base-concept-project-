from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from repositories.book_eligibility import ReturnBooksQuery

router = APIRouter(prefix="/return-books", tags=["ReturnBooks"])

# POST → Manager returns a book
@router.post("/")
def return_book(
    student_id: str = Query(..., description="Student ID"),
    book_id: str = Query(..., description="Book ID"),
    employee_id: str = Query(..., description="Manager Employee ID"),
    status_flag: str = Query(..., description="Book status after return (Available/Not Available)"),
    db: Session = Depends(get_db)
):
    return ReturnBooksQuery.return_book(student_id, book_id, employee_id, status_flag, db)

