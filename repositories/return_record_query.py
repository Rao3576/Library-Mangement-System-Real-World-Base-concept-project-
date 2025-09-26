from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import return_record

class ReturnQuery:

    @staticmethod
    def create_return_query(ret: return_record.BookReturnCreate, db: Session):
        sql = text("""
            INSERT INTO `Book-Return_record` (Return_id, Borrow_id, Return_date, `Condition`, Employee_id)
            VALUES (:Return_id, :Borrow_id, :Return_date, :Condition, :Employee_id)
        """)
        db.execute(sql, ret.dict())
        db.commit()
        return ReturnQuery.get_return_query(ret.Return_id, db)

    @staticmethod
    def list_returns_query(db: Session):
        result = db.execute(text("SELECT * FROM `Book-Return_record`")).fetchall()
        return [dict(r._mapping) for r in result]

    @staticmethod
    def get_return_query(return_id: str, db: Session):
        result = db.execute(
            text("SELECT * FROM `Book-Return_record` WHERE Return_id = :id"),
            {"id": return_id}
        ).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_return_query(return_id: str, ret: return_record.BookReturnUpdate, db: Session):
        update_fields = ret.dict(exclude_unset=True)
        if not update_fields:
            return ReturnQuery.get_return_query(return_id, db)

        set_clause = ", ".join([f"`{f}` = :{f}" for f in update_fields])
        update_fields["id"] = return_id
        sql = text(f"UPDATE `Book-Return_record` SET {set_clause} WHERE Return_id = :id")
        db.execute(sql, update_fields)
        db.commit()
        return ReturnQuery.get_return_query(return_id, db)

    @staticmethod
    def delete_return_query(return_id: str, db: Session):
        db.execute(text("DELETE FROM `Book-Return_record` WHERE Return_id = :id"), {"id": return_id})
        db.commit()
        return {"deleted_id": return_id}
