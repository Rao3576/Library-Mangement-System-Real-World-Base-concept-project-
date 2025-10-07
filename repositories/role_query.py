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
