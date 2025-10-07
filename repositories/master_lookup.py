from sqlalchemy.orm import Session
from sqlalchemy import text

class MasterLookupQuery:

    @staticmethod
    def get_all_master_data(db: Session ,model_name: str =None ,filter_name: str =None):
        data = {}

        tables = {
            "students": {"table": "Student", "name_field": "student_name"},
            "books": {"table": "Book", "name_field": "Title"},
            "authors": {"table": "Author", "name_field": "Author_name"},
            "publishers": {"table": "Publisher", "name_field": "Publisher_name"},
            "employees": {"table": "Employee", "name_field": "Employee_name"},
        }

        for key, info in tables.items():
            table = info["table"]
            name_field = info["name_field"]

            if filter_name:
                sql = text(f"SELECT * FROM {table} WHERE {name_field} LIKE :filter")
                result = db.execute(sql, {"filter": f"%{filter_name}%"}).mappings().all()
            else:
                sql = text(f"SELECT * FROM {table}")
                result = db.execute(sql).mappings().all()

            data[key] = [dict(row) for row in result]

        return data
