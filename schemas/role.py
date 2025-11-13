from pydantic import BaseModel
from typing import Optional, List

# ✅ Role Schemas
class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int

    
class RoleOut(RoleBase):
    id: int

    class Config:
        from_attributes = True  # (formerly orm_mode=True in Pydantic v1)
  







# class RoleCreate(BaseModel):
#     name: str
#     description: Optional[str] = None

# class RoleOut(BaseModel):
#     id: int
#     name: str
#     description: Optional[str] = None

#     class Config:
#         from_attributes = True  # For SQLAlchemy integration
