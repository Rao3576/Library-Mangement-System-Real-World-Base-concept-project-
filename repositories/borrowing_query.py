from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import borrowing

class BorrowingQuery:

    @staticmethod
    def create_borrowing_query(borrow: borrowing.BorrowingCreate, db: Session):
        sql = text("""
            INSERT INTO Borrowing (Borrowing_id, Student_id, Book_id, Employee_id, Borrow_date, Due_date)
            VALUES (:Borrowing_id, :Student_id, :Book_id, :Employee_id, :Borrow_date, :Due_date)
        """)
        db.execute(sql, borrow.dict())
        db.commit()
        return BorrowingQuery.get_borrowing_query(borrow.Borrowing_id, db)

    @staticmethod
    def list_borrowings_query(db: Session):
        result = db.execute(text("SELECT * FROM Borrowing")).fetchall()
        return [dict(r._mapping) for r in result]

    @staticmethod
    def get_borrowing_query(borrow_id: str, db: Session):
        result = db.execute(
            text("SELECT * FROM Borrowing WHERE Borrowing_id = :id"),
            {"id": borrow_id}
        ).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_borrowing_query(borrow_id: str, borrow: borrowing.BorrowingUpdate, db: Session):
        update_fields = borrow.dict(exclude_unset=True)
        if not update_fields:
            return BorrowingQuery.get_borrowing_query(borrow_id, db)

        set_clause = ", ".join([f"{f} = :{f}" for f in update_fields])
        update_fields["id"] = borrow_id
        sql = text(f"UPDATE Borrowing SET {set_clause} WHERE Borrowing_id = :id")
        db.execute(sql, update_fields)
        db.commit()
        return BorrowingQuery.get_borrowing_query(borrow_id, db)

    @staticmethod
    def delete_borrowing_query(borrow_id: str, db: Session):
        db.execute(text("DELETE FROM Borrowing WHERE Borrowing_id = :id"), {"id": borrow_id})
        db.commit()
        return {"deleted_id": borrow_id}
