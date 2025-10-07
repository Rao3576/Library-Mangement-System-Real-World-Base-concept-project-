from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import status
from authlib.integrations.starlette_client import OAuth
from config.config import settings
from models.auth_user import User
from utils.auth_user import create_tokens, decode_token, blacklist_token

oauth = OAuth()
oauth.register(
    name="google",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    access_token_url="https://oauth2.googleapis.com/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    api_base_url="https://www.googleapis.com/oauth2/v2/",
    client_kwargs={"scope": "openid email profile"},
)


class GoogleOAuthQuery:

    # ✅ Step 1: Redirect to Google Login
    @staticmethod
    async def google_login(request):
        redirect_uri = "http://localhost:8000/Oauth/auth/google/callback"
        redirect_response = await oauth.google.authorize_redirect(request, redirect_uri)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Redirecting to Google for authentication",
                "redirect_url": redirect_response.headers.get("location"),
            },
        )

    # ✅ Step 2: Handle Callback and Login
    @staticmethod
    async def google_callback(request, db: Session):
        try:
            token = await oauth.google.authorize_access_token(request)
            user_info = await oauth.google.parse_id_token(request, token)

            if not user_info or "email" not in user_info:
                return JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={"message": "Google login failed — no email found"},
                )

            email = user_info["email"]
            user = db.query(User).filter(User.email == email).first()

            if not user:
                user = User(
                    email=email,
                    is_verified=True,
                    is_active=True,
                    login_provider="google"
                )
                db.add(user)
                db.commit()
                db.refresh(user)

            access_token, refresh_token = create_tokens({"id": user.id, "email": user.email})
            user.refresh_token = refresh_token
            db.commit()

            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "message": "Login successful via Google OAuth2",
                    "data": {"user_id": user.id, "email": user.email},
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "token_type": "bearer",
                },
            )

        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"message": f"OAuth error: {str(e)}"},
            )

    # ✅ Step 3: Refresh Token
    @staticmethod
    async def refresh_access_token(refresh_token: str, db: Session):
        try:
            payload = decode_token(refresh_token)
            if not payload:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"message": "Invalid or expired refresh token"},
                )

            user = db.query(User).filter(User.email == payload.get("email")).first()
            if not user or user.refresh_token != refresh_token:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"message": "Unauthorized — token mismatch"},
                )

            new_access_token, new_refresh_token = create_tokens(
                {"id": user.id, "email": user.email}
            )
            user.refresh_token = new_refresh_token
            db.commit()

            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "message": "Access token refreshed successfully",
                    "access_token": new_access_token,
                    "refresh_token": new_refresh_token,
                },
            )

        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"message": f"Token refresh failed: {str(e)}"},
            )

    # ✅ Step 4: Logout (Blacklist tokens)
    @staticmethod
    async def logout_user(token: str, db: Session):
        try:
            payload = decode_token(token)
            if not payload:
                return JSONResponse(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    content={"message": "Invalid token"},
                )

            user = db.query(User).filter(User.email == payload.get("email")).first()
            if user:
                user.refresh_token = None
                db.commit()

            blacklist_token(token)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"message": "Logout successful. Tokens invalidated."},
            )

        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"message": f"Logout failed: {str(e)}"},
            )

