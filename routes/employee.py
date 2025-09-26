from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import employee
from repositories.employee_query import EmployeeQuery

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=employee.Employee)
def create_employee(employee: employee.EmployeeCreate, db: Session = Depends(get_db)):
    return EmployeeQuery.create_employee_query(employee, db)

@router.get("/", response_model=list[employee.Employee])
def list_employees(db: Session = Depends(get_db)):
    return EmployeeQuery.list_employees_query(db)

@router.get("/{employee_id}", response_model=employee.Employee)
def get_employee(employee_id: str, db: Session = Depends(get_db)):
    emp = EmployeeQuery.get_employee_query(employee_id, db)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@router.put("/{employee_id}", response_model=employee.Employee)
def update_employee(employee_id: str, employee: employee.EmployeeUpdate, db: Session = Depends(get_db)):
    updated = EmployeeQuery.update_employee_query(employee_id, employee, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated

@router.delete("/{employee_id}")
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    deleted = EmployeeQuery.delete_employee_query(employee_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted

