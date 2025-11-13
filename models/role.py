from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import relationship
from database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(String(255), primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)

    # Relationships
    user_roles = relationship("UserRole", back_populates="role")  # ← singular
    permissions = relationship("Permission", back_populates="role")  # ← singular





# class permission(Base):
#     __tablename__ = "permission"

#     id = Column(Integer, primary_key=True, index=True)
#     permissions = Column(JSON, unique=True, nullable=False)
#     role_id = Column(BigInteger,ForeignKey("roles.id"), nullable=True)
#       # ✅ Back relationship to users
#     users = relationship("User", back_populates="roles")