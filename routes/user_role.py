from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repositories.user_role import UserRoleQuery
from fastapi.responses import JSONResponse

# ✅ Create router instance
router = APIRouter(
    prefix="/user-role",
    tags=["User Role Management"]
)

# # ✅ Assign a role to a user
# @router.post("/assign")
# def assign_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
#     result = UserRoleQuery.assign_role(db, user_id, role_id)
#     return JSONResponse(content=result, status_code=200)

# # ✅ Get all roles for a user
# @router.get("/user/{user_id}")
# def get_user_roles(user_id: int, db: Session = Depends(get_db)):
#     result = UserRoleQuery.get_user_roles(db, user_id)
#     return JSONResponse(content=result, status_code=200)








# ✅ UserRole Routes
@router.post("/assign")
def assign_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    return UserRoleQuery.assign_role(db, user_id, role_id)

@router.get("/user/{user_id}")
def get_user_roles(user_id: int, db: Session = Depends(get_db)):
    return UserRoleQuery.get_user_roles(db, user_id)

