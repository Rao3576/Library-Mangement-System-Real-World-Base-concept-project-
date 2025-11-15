# from fastapi.responses import JSONResponse
# from fastapi import HTTPException
# from sqlalchemy.orm import Session
# from models.role import Role


# # ✅ Role CRUD
# class RoleQuery:
#     @staticmethod
#     def create_role(db: Session, name: str, description: str = None):
#         new_role = Role(name=name, description=description)
#         db.add(new_role)
#         db.commit()
#         db.refresh(new_role)
#         return JSONResponse(content={"message": "Role created", "data": {"id": new_role.id, "name": new_role.name}}, status_code=201)

#     @staticmethod
#     def get_roles(db: Session):
#         roles = db.query(Role).all()
#         return JSONResponse(content={"data": [ {"id": r.id, "name": r.name, "description": r.description} for r in roles ]})

#     @staticmethod
#     def delete_role(db: Session, role_id: int):
#         role = db.query(Role).filter(Role.id == role_id).first()
#         if not role:
#             raise HTTPException(status_code=404, detail="Role not found")
#         db.delete(role)
#         db.commit()
#         return JSONResponse(content={"message": "Role deleted"})







from sqlalchemy.orm import Session
from models.role import Role

def create_role_query(db: Session, name: str, description: str = None):
    new_role = Role(name=name, description=description)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def get_roles_query(db: Session):
    return db.query(Role).all()

def update_role_query(db: Session, role_id: int, name: str, description: str):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        return None
    role.name = name
    role.description = description
    db.commit()
    db.refresh(role)
    return role

def delete_role_query(db: Session, role_id: int):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        return None
    db.delete(role)
    db.commit()
    return True
