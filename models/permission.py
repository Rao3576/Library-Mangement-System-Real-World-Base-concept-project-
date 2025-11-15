from sqlalchemy import Column, BigInteger, JSON, ForeignKey,Integer,String
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Permission(Base):
    __tablename__ = "permissions"

    id = Column(String(255), primary_key=True)
    permissions = Column(JSON, nullable=False)
    role_id = Column(String(255), ForeignKey("roles.id"), nullable=False)

    role = relationship("Role", back_populates="permissions")


