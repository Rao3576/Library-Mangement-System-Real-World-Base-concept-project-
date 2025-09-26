from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import report
from repositories.report import ReportQuery

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.post("/", response_model=report.Report)
def create_report(report: report.ReportCreate, db: Session = Depends(get_db)):
    return ReportQuery.create_report_query(report, db)

@router.get("/", response_model=list[report.Report])
def list_reports(db: Session = Depends(get_db)):
    return ReportQuery.list_reports_query(db)

@router.get("/{report_id}", response_model=report.Report)
def get_report(report_id: str, db: Session = Depends(get_db)):
    r = ReportQuery.get_report_query(report_id, db)
    if not r:
        raise HTTPException(status_code=404, detail="Report not found")
    return r

@router.put("/{report_id}", response_model=report.Report)
def update_report(report_id: str, report: report.ReportUpdate, db: Session = Depends(get_db)):
    updated = ReportQuery.update_report_query(report_id, report, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Report not found")
    return updated

@router.delete("/{report_id}")
def delete_report(report_id: str, db: Session = Depends(get_db)):
    return ReportQuery.delete_report_query(report_id, db)
