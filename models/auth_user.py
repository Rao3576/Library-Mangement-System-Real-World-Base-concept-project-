from sqlalchemy.orm import relationship
import uuid
from sqlalchemy import Column, String, Boolean
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    user_roles = relationship("UserRole", back_populates="user")











# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String(255), unique=True, nullable=False)
#    # name = Column(String(255), nullable=True)
#     hashed_password = Column(String(255), nullable=True)
#     is_verified = Column(Boolean, default=False)
#     is_active = Column(Boolean, default=True)
#     login_provider = Column(String(50), default="local")  # 'local' or 'google'
#     login_provider = Column(String(50), nullable=True)  # ✅ the missing column
#     refresh_token = Column(String(500), nullable=True)  # ✅ store latest refresh token
#   # ✅ Correct relationship
#     roles = relationship("Role", back_populates="users")
