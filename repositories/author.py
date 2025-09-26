from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import author

class AuthorQuery:

    @staticmethod
    def create_author_query(author: author.AuthorCreate, db: Session):
        sql = text("""
            INSERT INTO Author (Author_id, Author_name, Bio, Nationality)
            VALUES (:Author_id, :Author_name, :Bio, :Nationality)
        """)
        db.execute(sql, author.dict())
        db.commit()
        return AuthorQuery.get_author_query(author.Author_id, db)

    @staticmethod
    def list_authors_query(db: Session):
        sql = text("SELECT * FROM Author")
        result = db.execute(sql).fetchall()
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_author_query(author_id: str, db: Session):
        sql = text("SELECT * FROM Author WHERE Author_id = :Author_id")
        result = db.execute(sql, {"Author_id": author_id}).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_author_query(author_id: str, author: author.AuthorUpdate, db: Session):
        update_fields = author.dict(exclude_unset=True)
        if not update_fields:
            return AuthorQuery.get_author_query(author_id, db)

        set_clause = ", ".join([f"{f} = :{f}" for f in update_fields])
        sql = text(f"UPDATE Author SET {set_clause} WHERE Author_id = :Author_id")
        update_fields["Author_id"] = author_id
        db.execute(sql, update_fields)
        db.commit()
        return AuthorQuery.get_author_query(author_id, db)

    @staticmethod
    def delete_author_query(author_id: str, db: Session):
        sql = text("DELETE FROM Author WHERE Author_id = :Author_id")
        db.execute(sql, {"Author_id": author_id})
        db.commit()
        return {"deleted_id": author_id}
