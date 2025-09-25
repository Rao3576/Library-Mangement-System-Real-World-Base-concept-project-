from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import student
from repositories.student_query import StudentQuery

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=student.Student)
def create_student(student:student.StudentCreate, db: Session = Depends(get_db)):
    return StudentQuery.create_student_query(student, db)

@router.get("/", response_model=list[student.Student])
def list_students(db: Session = Depends(get_db)):
    return StudentQuery.list_students_query(db)

@router.get("/{student_id}", response_model=student.Student)
def get_student(student_id: str, db: Session = Depends(get_db)):
    student = StudentQuery.get_student_query(student_id, db)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=student.Student)
def update_student(student_id: str, student: student.StudentUpdate, db: Session = Depends(get_db)):
    updated_student = StudentQuery.update_student_query(student_id, student, db)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found or no fields to update")
    return updated_student

@router.delete("/{student_id}")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    deleted = StudentQuery.delete_student_query(student_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted successfully"}

