from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import publishers


class PublisherQuery:

    @staticmethod
    def create_publisher_query(publisher: publishers.PublisherCreate, db: Session):
        sql = text("""
            INSERT INTO Publisher (Publisher_id, Publisher_name, Address, Email, Phone)
            VALUES (:Publisher_id, :Publisher_name, :Address, :Email, :Phone)
        """)
        db.execute(sql, publisher.dict())
        db.commit()
        return PublisherQuery.get_publisher_query(publisher.Publisher_id, db)

    @staticmethod
    def list_publishers_query(db: Session):
        sql = text("SELECT * FROM Publisher")
        result = db.execute(sql).fetchall()
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_publisher_query(publisher_id: str, db: Session):
        sql = text("SELECT * FROM Publisher WHERE Publisher_id = :Publisher_id")
        result = db.execute(sql, {"Publisher_id": publisher_id}).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_publisher_query(publisher_id: str, publisher: publishers.PublisherUpdate, db: Session):
        update_fields = publisher.dict(exclude_unset=True)
        if not update_fields:
            return PublisherQuery.get_publisher_query(publisher_id, db)

        set_clause = ", ".join([f"{field} = :{field}" for field in update_fields.keys()])
        sql = text(f"UPDATE Publisher SET {set_clause} WHERE Publisher_id = :Publisher_id")
        update_fields["Publisher_id"] = publisher_id
        db.execute(sql, update_fields)
        db.commit()
        return PublisherQuery.get_publisher_query(publisher_id, db)

    @staticmethod
    def delete_publisher_query(publisher_id: str, db: Session):
        sql = text("DELETE FROM Publisher WHERE Publisher_id = :Publisher_id")
        db.execute(sql, {"Publisher_id": publisher_id})
        db.commit()
        return {"deleted_id": publisher_id}
