from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from schemas import student
from fastapi.responses import JSONResponse
from repositories.student_query import StudentQuery

router = APIRouter(prefix="", tags=["Students"])

@router.post("/create-student", response_model=student.Student)
def create_student(student: student.StudentCreate, db: Session = Depends(get_db)):
    return StudentQuery.create_student_query(student, db)

@router.get("/get-all-students", response_model=list[student.Student])
def list_students(db: Session = Depends(get_db)):
    return StudentQuery.list_students_query(db)

@router.get("/get-student-byid/{id}", response_model=student.Student)
def get_student(id: str, db: Session = Depends(get_db)):
    student_data = StudentQuery.get_student_query(id, db)
    if not student_data:
        raise HTTPException(status_code=404, detail="Student not found")
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": "students data fetched successfully",
            "data": student_data
        }
    )


@router.put("/update-student-byid/{id}", response_model=student.Student)
def update_student(id: str, student: student.StudentUpdate, db: Session = Depends(get_db)):
    updated_student = StudentQuery.update_student_query(id, student, db)
    if not updated_student:
        raise HTTPException(status_code=404, detail="Student not found or no fields to update")
    return updated_student

@router.delete("/delete-student/{id}")
def delete_student(id: str, db: Session = Depends(get_db)):
    deleted = StudentQuery.delete_student_query(id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"detail": "Student deleted successfully"}





