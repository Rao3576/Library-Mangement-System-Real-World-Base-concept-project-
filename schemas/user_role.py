from pydantic import BaseModel
from typing import Optional, List

# ✅ UserRole Schemas
class UserRoleBase(BaseModel):
    user_id: int
    role_id: int

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleResponse(UserRoleBase):
    id: int
    class Config:
        from_attributes = True



