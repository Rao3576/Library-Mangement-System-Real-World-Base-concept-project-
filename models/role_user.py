from sqlalchemy import Column, Integer, ForeignKey,BigInteger,String
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# ✅ Many-to-Many relationship bridge table
class UserRole(Base):
    __tablename__ = "user_roles"

    user_id = Column(String(255), ForeignKey("users.id"), primary_key=True)
    role_id = Column(String(255), ForeignKey("roles.id"), primary_key=True)

    # Relationships
    user = relationship("User", back_populates="user_roles")
    role = relationship("Role", back_populates="user_roles")

