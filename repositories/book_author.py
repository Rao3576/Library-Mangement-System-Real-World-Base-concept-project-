from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import book_author

class BookAuthorQuery:

    @staticmethod
    def create_book_author_query(ba: book_author.BookAuthorCreate, db: Session):
        sql = text("""
            INSERT INTO Book_Author (Book_id, Author_id)
            VALUES (:Book_id, :Author_id)
        """)
        db.execute(sql, ba.dict())
        db.commit()
        return BookAuthorQuery.get_book_author_query(ba.Book_id, ba.Author_id, db)

    @staticmethod
    def list_book_authors_query(db: Session):
        result = db.execute(text("SELECT * FROM Book_Author")).fetchall()
        return [dict(r._mapping) for r in result]

    @staticmethod
    def get_book_author_query(book_id: str, author_id: str, db: Session):
        result = db.execute(
            text("SELECT * FROM Book_Author WHERE Book_id = :bid AND Author_id = :aid"),
            {"bid": book_id, "aid": author_id}
        ).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def delete_book_author_query(book_id: str, author_id: str, db: Session):
        db.execute(
            text("DELETE FROM Book_Author WHERE Book_id = :bid AND Author_id = :aid"),
            {"bid": book_id, "aid": author_id}
        )
        db.commit()
        return {"deleted": {"Book_id": book_id, "Author_id": author_id}}

