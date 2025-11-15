from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repositories.permission_query import PermissionQuery
from fastapi.responses import JSONResponse

# ✅ Create router instance
router = APIRouter(
    prefix="/permission",
    tags=["Permission Management"]
)

# # ✅ Create a new permission
# @router.post("/create")
# def create_permission(role_id: int, name: str, description: str = None, db: Session = Depends(get_db)):
#     result = PermissionQuery.create_permission(db, role_id, name, description)
#     return JSONResponse(content=result, status_code=200)

# # ✅ Get permissions for a specific role
# @router.get("/{role_id}")
# def get_permissions(role_id: int, db: Session = Depends(get_db)):
#     result = PermissionQuery.get_permissions(db, role_id)
#     return JSONResponse(content=result, status_code=200)








# ✅ Permission Routes
@router.post("/permission/create")
def create_permission(role_id: int, name: str, description: str = None, db: Session = Depends(get_db)):
    return PermissionQuery.create_permission(db, role_id, name, description)

@router.get("/permission/{role_id}")
def get_permissions(role_id: int, db: Session = Depends(get_db)):
    return PermissionQuery.get_permissions(db, role_id)