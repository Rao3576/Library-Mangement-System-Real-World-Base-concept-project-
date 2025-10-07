from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import bookstatus

class BookStatusQuery:

    @staticmethod
    def create_status_query(status: bookstatus.BookStatusCreate, db: Session):
        sql = text("""
            INSERT INTO book_status (Status_id, Book_id, Status, Last_update)
            VALUES (:Status_id, :Book_id, :Status, :Last_update)
        """)
        db.execute(sql, {
            "Status_id": status.Status_id,
            "Book_id": status.Book_id,
            "Status": status.Status,
            "Last_update": status.Last_update
        })
        db.commit()
        return BookStatusQuery.get_status_query(status.Status_id, db)


    @staticmethod
    def list_statuses_query(db: Session):
        result = db.execute(text("SELECT * FROM book_status")).fetchall()
        return [dict(r._mapping) for r in result]

    @staticmethod
    def get_status_query(status_id: str, db: Session):
        result = db.execute(
            text("SELECT * FROM book_status WHERE Status_id = :id"),
            {"id": status_id}
        ).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_status_query(status_id: str, status: bookstatus.BookStatusUpdate, db: Session):
        update_fields = status.dict(exclude_unset=True)
        if not update_fields:
            return BookStatusQuery.get_status_query(status_id, db)

        set_clause = ", ".join([f"{f} = :{f}" for f in update_fields])
        update_fields["id"] = status_id
        sql = text(f"UPDATE book_status SET {set_clause} WHERE Status_id = :id")
        db.execute(sql, update_fields)
        db.commit()
        return BookStatusQuery.get_status_query(status_id, db)

    @staticmethod
    def delete_status_query(status_id: str, db: Session):
        db.execute(text("DELETE FROM book_status WHERE Status_id = :id"), {"id": status_id})
        db.commit()
        return {"deleted_id": status_id}
