from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import bookstatus

class BookStatusQuery:

    @staticmethod
    def create_status_query(status: bookstatus.BookStatusCreate, db: Session):
        sql = text("""
            INSERT INTO BookStatus (Status_id, Book_id, Availability, Condition)
            VALUES (:Status_id, :Book_id, :Availability, :Condition)
        """)
        db.execute(sql, status.dict())
        db.commit()
        return BookStatusQuery.get_status_query(status.Status_id, db)

    @staticmethod
    def list_statuses_query(db: Session):
        result = db.execute(text("SELECT * FROM BookStatus")).fetchall()
        return [dict(r._mapping) for r in result]

    @staticmethod
    def get_status_query(status_id: str, db: Session):
        result = db.execute(
            text("SELECT * FROM BookStatus WHERE Status_id = :id"),
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
        sql = text(f"UPDATE BookStatus SET {set_clause} WHERE Status_id = :id")
        db.execute(sql, update_fields)
        db.commit()
        return BookStatusQuery.get_status_query(status_id, db)

    @staticmethod
    def delete_status_query(status_id: str, db: Session):
        db.execute(text("DELETE FROM BookStatus WHERE Status_id = :id"), {"id": status_id})
        db.commit()
        return {"deleted_id": status_id}
