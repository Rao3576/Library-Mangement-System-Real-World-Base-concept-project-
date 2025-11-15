from pydantic import BaseModel
from typing import Optional ,List

# ✅ Permission Schemas
class PermissionBase(BaseModel):
    role_id: int
    name: str
    description: Optional[str] = None

class PermissionCreate(PermissionBase):
    pass

class PermissionResponse(PermissionBase):
    id: int
    class Config:
        from_attributes = True
