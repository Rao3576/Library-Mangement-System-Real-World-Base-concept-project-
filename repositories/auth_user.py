from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
import models.auth_user
import schemas.auth_user
import utils.auth_user
import utils.verify_email
from models.auth_user import User
from utils.auth_user import (hash_password)
from utils.token_utils import (
    create_reset_token,
    verify_reset_token,
    send_email
)


class UserQuery:

    @staticmethod
    def register_user(user: schemas.auth_user.UserCreate, db: Session):
        # Check if user already exists
        db_user = db.query(models.auth_user.User).filter(models.auth_user.User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Hash password and create user
        hashed = utils.auth_user.hash_password(user.password)
        new_user = models.auth_user.User(email=user.email, hashed_password=hashed)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # Send verification email
        token = utils.auth_user.email_create_token({"sub": user.email})
        utils.verify_email.send_verification_email(user.email, token)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "Please check your email to verify your account."
            }
        )

    @staticmethod
    def verify_email(token: str, db: Session):        
        data = utils.auth_user.decode_token(token)
        if not data:
            raise HTTPException(status_code=400, detail="Invalid or expired token")

        user = db.query(models.auth_user.User).filter(models.auth_user.User.email == data["sub"]).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.is_verified = True
        db.commit()

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "Email verified successfully!"
            }
        )

    @staticmethod
    def login_user(form_data: schemas.auth_user.UserLogin, db: Session):
        user = db.query(models.auth_user.User).filter(models.auth_user.User.email == form_data.email).first()

        if not user or not utils.auth_user.verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        if not user.is_verified:
            raise HTTPException(status_code=401, detail="Email not verified")

        # Convert SQLAlchemy model → Pydantic schema
        user_data = schemas.auth_user.UserOut.model_validate(user)
        user_dict = user_data.model_dump()

        # Create tokens
        access_token, refresh_token = utils.auth_user.create_tokens({"sub": user.email})

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "User logged in successfully",
                "data": user_dict,
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer"
            }
        )


    # ✅ Send password reset link
    @staticmethod
    def send_reset_password_email(email: str, db: Session):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="No user found with this email")

        reset_token = create_reset_token({"sub": user.email})
        reset_link = f"http://localhost:8000/user/reset-password?token={reset_token}"

        # send reset email
        send_email(user.email, "reset", reset_link)

        return JSONResponse(
            content={"message": f"Password reset link sent to {user.email}"},
            status_code=200
        )

    # ✅ Reset password
    @staticmethod
    def reset_user_password(token: str, new_password: str, db: Session):
        payload = verify_reset_token(token)
        if not payload:
            raise HTTPException(status_code=400, detail="Invalid or expired token")

        user = db.query(User).filter(User.email == payload["sub"]).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user.hashed_password = hash_password(new_password)
        db.commit()

        return JSONResponse(
            content={"message": "Password has been reset successfully"},
            status_code=200
        )
