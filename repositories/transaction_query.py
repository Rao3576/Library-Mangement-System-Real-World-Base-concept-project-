from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import transaction

class TransactionQuery:

    @staticmethod
    def create_transaction_query(tx: transaction.TransactionCreate, db: Session):
        sql = text("""
            INSERT INTO Transaction (Transaction_id, Student_id, Transaction_Type, Account, Transaction_date)
            VALUES (:Transaction_id, :Student_id, :Transaction_Type, :Account, :Transaction_date)
        """)
        db.execute(sql, tx.dict())
        db.commit()
        return TransactionQuery.get_transaction_query(tx.Transaction_id, db)

    @staticmethod
    def list_transactions_query(db: Session):
        result = db.execute(text("SELECT * FROM Transaction")).fetchall()
        return [dict(r._mapping) for r in result]

    @staticmethod
    def get_transaction_query(tx_id: str, db: Session):
        result = db.execute(
            text("SELECT * FROM Transaction WHERE Transaction_id = :id"),
            {"id": tx_id}
        ).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_transaction_query(tx_id: str, tx: transaction.TransactionUpdate, db: Session):
        update_fields = tx.dict(exclude_unset=True)
        if not update_fields:
            return TransactionQuery.get_transaction_query(tx_id, db)

        set_clause = ", ".join([f"{f} = :{f}" for f in update_fields])
        update_fields["id"] = tx_id
        sql = text(f"UPDATE Transaction SET {set_clause} WHERE Transaction_id = :id")
        db.execute(sql, update_fields)
        db.commit()
        return TransactionQuery.get_transaction_query(tx_id, db)

    @staticmethod
    def delete_transaction_query(tx_id: str, db: Session):
        db.execute(text("DELETE FROM Transaction WHERE Transaction_id = :id"), {"id": tx_id})
        db.commit()
        return {"deleted_id": tx_id}
