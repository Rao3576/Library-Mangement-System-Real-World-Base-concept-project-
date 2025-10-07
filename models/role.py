from sqlalchemy import Column, Integer, String,JSON
from database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    # user_id = Column(biginteger,foreignkey("users.id"), nullable=True)
    # users=relationship("User",backpopulates="roles")
#     permission=relationship("Permission",backpopulates="roles")

# class permission(Base):
#     __tablename__ = "permission"

#     id = Column(Integer, primary_key=True, index=True)
#     permissions = Column(JSON, unique=True, nullable=False)
#     role_id = Column(biginteger,foreignkey("roles.id"), nullable=True)
#     roles=relationship("Role",backpopulates="permission")