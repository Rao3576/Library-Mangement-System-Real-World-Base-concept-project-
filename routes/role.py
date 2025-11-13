# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from database import get_db
# from repositories.role_query import RoleQuery

# router = APIRouter(prefix="/role", tags=["Role & Permission"])


# # ✅ Role Routes
# @router.post("/create")
# def create_role(name: str, description: str = None, db: Session = Depends(get_db)):
#     return RoleQuery.create_role(db, name, description)

# @router.get("/list")
# def get_roles(db: Session = Depends(get_db)):
#     return RoleQuery.get_roles(db)


# @router.delete("/{role_id}")
# def delete_role(role_id: int, db: Session = Depends(get_db)):
#     return RoleQuery.delete_role(db, role_id)






from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database import get_db
from schemas.role import RoleCreate, RoleOut
from repositories.role_query import (
    create_role_query,
    get_roles_query,
    update_role_query,
    delete_role_query
)
from utils.dependencies import require_role_in
from typing import List

router = APIRouter(prefix="/roles", tags=["Roles"])

# Create Role
@router.post("/", response_model=RoleOut)
def create_role(role: RoleCreate, db: Session = Depends(get_db),
                current_user=Depends(require_role_in(["admin"]))):
    
    new_role = create_role_query(db, role.name, role.description)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": True, "data": new_role.__dict__})

# Get Roles
@router.get("/", response_model=List[RoleOut])
def read_roles(db: Session = Depends(get_db),
               current_user=Depends(require_role_in(["admin", "manager"]))):
    roles = get_roles_query(db)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": True, "data": [r.__dict__ for r in roles]})

# Update Role
@router.put("/{role_id}", response_model=RoleOut)
def update_role(role_id: int, role: RoleCreate,
                db: Session = Depends(get_db),
                current_user=Depends(require_role_in(["admin"]))):
    updated = update_role_query(db, role_id, role.name, role.description)
    if not updated:
        raise HTTPException(status_code=404, detail="Role not found")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": True, "data": updated.__dict__})

# Delete Role
@router.delete("/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db),
                current_user=Depends(require_role_in(["admin"]))):
    deleted = delete_role_query(db, role_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Role not found")
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": True, "message": "Role deleted successfully"})
