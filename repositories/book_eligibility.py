from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi.responses import JSONResponse
from fastapi import status
import datetime

class ReturnBooksQuery:

    @staticmethod
    def return_book(student_id: str, book_id: str, employee_id: str, status_flag: str, db: Session):
        # ✅ Step 1: Check employee is Manager
        emp_check = db.execute(
            text("SELECT * FROM Employee WHERE Employee_id = :eid AND Position = 'Manager'"),
            {"eid": employee_id}
        ).mappings().first()
        if not emp_check:
            return JSONResponse(
                status_code=status.HTTP_403_FORBIDDEN,
                content={
                    "status_code": status.HTTP_403_FORBIDDEN,
                    "message": "Only Manager can return books",
                }
            )

        # ✅ Step 2: Check if Borrowing exists for this student & book
        borrow_check = db.execute(
            text("SELECT * FROM Borrowing WHERE Student_id = :sid AND Book_id = :bid"),
            {"sid": student_id, "bid": book_id}
        ).mappings().first()
        if not borrow_check:
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "No borrowing record found for this student and book",
                }
            )

        # ✅ Step 3: Insert into BookReturnRecord
        return_id = f"RET_{student_id}_{book_id}_{int(datetime.datetime.now().timestamp())}"
        db.execute(text("""
            INSERT INTO BookReturnRecord (Return_id, Borrowing_id, Return_date, Status)
            VALUES (:Return_id, :Borrowing_id, :Return_date, :Status)
        """), {
            "Return_id": return_id,
            "Borrowing_id": borrow_check["Borrowing_id"],
            "Return_date": datetime.date.today(),
            "Status": status_flag
        })

        # ✅ Step 4: Update BookStatus
        db.execute(text("""
            UPDATE BookStatus
            SET Status = :Status
            WHERE Book_id = :bid
        """), {"Status": status_flag, "bid": book_id})

        db.commit()

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "Book returned successfully",
                "data": {
                    "Return_id": return_id,
                    "Student_id": student_id,
                    "Book_id": book_id,
                    "Returned_by": employee_id,
                    "Return_date": str(datetime.date.today()),
                    "Book_status": status_flag
                }
            }
        )

