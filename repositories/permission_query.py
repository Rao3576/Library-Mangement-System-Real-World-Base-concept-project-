from fastapi.responses import JSONResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.permission import Permission

# ✅ Permission CRUD
class PermissionQuery:
    @staticmethod
    def create_permission(db: Session, role_id: int, name: str, description: str = None):
        permission = Permission(role_id=role_id, name=name, description=description)
        db.add(permission)
        db.commit()
        db.refresh(permission)
        return JSONResponse(content={"message": "Permission created", "data": {"id": permission.id}}, status_code=201)

    @staticmethod
    def get_permissions(db: Session, role_id: int):
        permissions = db.query(Permission).filter(Permission.role_id == role_id).all()
        return JSONResponse(content={"data": [{"id": p.id, "name": p.name, "description": p.description} for p in permissions]})