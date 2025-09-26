from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import employee

class EmployeeQuery:

    @staticmethod
    def create_employee_query(employee: employee.EmployeeCreate, db: Session):
        sql = text("""
            INSERT INTO Employee (Employee_id, Employee_name, Email, phone, Position)
            VALUES (:Employee_id, :Employee_name, :Email, :phone, :Position)
        """)
        db.execute(sql, employee.dict())
        db.commit()
        return EmployeeQuery.get_employee_query(employee.Employee_id, db)

    @staticmethod
    def list_employees_query(db: Session):
        sql = text("SELECT * FROM Employee")
        result = db.execute(sql).fetchall()
        return [dict(row._mapping) for row in result]

    @staticmethod
    def get_employee_query(employee_id: str, db: Session):
        sql = text("SELECT * FROM Employee WHERE Employee_id = :Employee_id")
        result = db.execute(sql, {"Employee_id": employee_id}).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_employee_query(employee_id: str, employee: employee.EmployeeUpdate, db: Session):
        update_fields = employee.dict(exclude_unset=True)
        if not update_fields:
            return EmployeeQuery.get_employee_query(employee_id, db)

        set_clause = ", ".join([f"{f} = :{f}" for f in update_fields])
        sql = text(f"UPDATE Employee SET {set_clause} WHERE Employee_id = :Employee_id")
        update_fields["Employee_id"] = employee_id
        db.execute(sql, update_fields)
        db.commit()
        return EmployeeQuery.get_employee_query(employee_id, db)

    @staticmethod
    def delete_employee_query(employee_id: str, db: Session):
        sql = text("DELETE FROM Employee WHERE Employee_id = :Employee_id")
        db.execute(sql, {"Employee_id": employee_id})
        db.commit()
        return {"deleted_id": employee_id}
