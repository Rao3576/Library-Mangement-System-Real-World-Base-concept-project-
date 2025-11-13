from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.role_user import UserRole


# ✅ UserRole CRUD
class UserRoleQuery:
    @staticmethod
    def assign_role(db: Session, user_id: int, role_id: int):
        mapping = UserRole(user_id=user_id, role_id=role_id)
        db.add(mapping)
        db.commit()
        db.refresh(mapping)
        return JSONResponse(content={"message": "Role assigned to user", "data": {"id": mapping.id}}, status_code=201)

    @staticmethod
    def get_user_roles(db: Session, user_id: int):
        roles = db.query(UserRole).filter(UserRole.user_id == user_id).all()
        return JSONResponse(content={"data": [{"id": r.id, "role_id": r.role_id} for r in roles]})