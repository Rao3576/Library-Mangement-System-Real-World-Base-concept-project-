from sqlalchemy.orm import Session
from sqlalchemy import text
from schemas import report

class ReportQuery:

    @staticmethod
    def create_report_query(report: report.ReportCreate, db: Session):
        sql = text("""
            INSERT INTO Report (Report_id, Report_Type, Created_date, Student_id, Employee_id)
            VALUES (:Report_id, :Report_Type, :Created_date, :Student_id, :Employee_id)
        """)
        db.execute(sql, report.dict())
        db.commit()
        return ReportQuery.get_report_query(report.Report_id, db)

    @staticmethod
    def list_reports_query(db: Session):
        result = db.execute(text("SELECT * FROM Report")).fetchall()
        return [dict(r._mapping) for r in result]

    @staticmethod
    def get_report_query(report_id: str, db: Session):
        result = db.execute(
            text("SELECT * FROM Report WHERE Report_id = :id"),
            {"id": report_id}
        ).fetchone()
        return dict(result._mapping) if result else None

    @staticmethod
    def update_report_query(report_id: str, report: report.ReportUpdate, db: Session):
        update_fields = report.dict(exclude_unset=True)
        if not update_fields:
            return ReportQuery.get_report_query(report_id, db)

        set_clause = ", ".join([f"{f} = :{f}" for f in update_fields])
        update_fields["id"] = report_id
        sql = text(f"UPDATE Report SET {set_clause} WHERE Report_id = :id")
        db.execute(sql, update_fields)
        db.commit()
        return ReportQuery.get_report_query(report_id, db)

    @staticmethod
    def delete_report_query(report_id: str, db: Session):
        db.execute(text("DELETE FROM Report WHERE Report_id = :id"), {"id": report_id})
        db.commit()
        return {"deleted_id": report_id}
