from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import book


class BookQuery:

    @staticmethod
    def create_book_query(book: book.BookCreate, db: Session):
        sql = text("""
            INSERT INTO Book (Book_id, Title, Publication_Year, Edition, Publisher_id)
            VALUES (:Book_id, :Title, :Publication_Year, :Edition, :Publisher_id)
        """)
        db.execute(sql, book.dict())
        db.commit()
        return BookQuery.get_book_query(book.Book_id, db)

    @staticmethod
    def list_books_query(db: Session):
        sql = text("SELECT * FROM Book")
        result = db.execute(sql).fetchall()
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_book_query(book_id: str, db: Session):
        sql = text("SELECT * FROM Book WHERE Book_id = :Book_id")
        result = db.execute(sql, {"Book_id": book_id}).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_book_query(book_id: str, book: book.BookUpdate, db: Session):
        update_fields = book.dict(exclude_unset=True)
        if not update_fields:
            return BookQuery.get_book_query(book_id, db)

        set_clause = ", ".join([f"{field} = :{field}" for field in update_fields.keys()])
        sql = text(f"UPDATE Book SET {set_clause} WHERE Book_id = :Book_id")
        update_fields["Book_id"] = book_id
        db.execute(sql, update_fields)
        db.commit()
        return BookQuery.get_book_query(book_id, db)

    @staticmethod
    def delete_book_query(book_id: str, db: Session):
        sql = text("DELETE FROM Book WHERE Book_id = :Book_id")
        db.execute(sql, {"Book_id": book_id})
        db.commit()
        return {"deleted_id": book_id}
