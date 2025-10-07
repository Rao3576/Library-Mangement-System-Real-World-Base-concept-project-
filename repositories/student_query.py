from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import student

class StudentQuery:

    @staticmethod
    def create_student_query(student:student.StudentCreate, db: Session):
        query = text("""
            INSERT INTO Student (student_id, student_name, Email, Address, Status)
            VALUES (:student_id, :student_name, :Email, :Address, :Status)
        """)
        db.execute(query, {
            "student_id": student.student_id,
            "student_name": student.student_name,
            "Email": student.Email,
            "Address": student.Address,
            "Status": student.Status
        })
        db.commit()

        return {
            "student_id": student.student_id,
            "student_name": student.student_name,
            "Email": student.Email,
            "Address": student.Address,
            "Status": student.Status
        }

    @staticmethod
    def list_students_query(db: Session):
        query = text("SELECT * FROM Student")
        result = db.execute(query).mappings().all()
        return [dict(row) for row in result]

    @staticmethod
    def get_student_query(student_id: str, db: Session):
        query = text("SELECT * FROM Student WHERE student_id = :student_id")
        result = db.execute(query, {"student_id": student_id}).mappings().first()
        return dict(result) if result else None

    @staticmethod
    def update_student_query(student_id: str, student: student.StudentUpdate, db: Session):
        update_data = student.dict(exclude_unset=True)
        if not update_data:
            return None

        set_clause = ", ".join([f"{key} = :{key}" for key in update_data.keys()])
        update_data["student_id"] = student_id

        query = text(f"UPDATE Student SET {set_clause} WHERE student_id = :student_id")
        result = db.execute(query, update_data)
        db.commit()

        if result.rowcount == 0:
            return None
            

        return StudentQuery.get_student_query(student_id, db)

    @staticmethod
    def delete_student_query(student_id: str, db: Session):
        query = text("DELETE FROM Student WHERE student_id = :student_id")
        result = db.execute(query, {"student_id": student_id})
        db.commit()
        return result.rowcount > 0
