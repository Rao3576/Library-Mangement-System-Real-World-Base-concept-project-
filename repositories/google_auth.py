# repositories/google_auth_repository.py
from fastapi import HTTPException, status, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from authlib.integrations.starlette_client import OAuth
from config.config import settings
from models.auth_user import User
from utils.auth_user import create_token  # ✅ from your auth utils

# ✅ Initialize OAuth
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

class GoogleAuthQuery:
    @staticmethod
    async def get_login_url(request: Request):
        """Step 1: Generate Google login URL (for browser / manual testing)."""
        redirect_uri = "http://localhost:8000/Oauth/auth/google/callback"

        # ✅ Reset old session to prevent mismatching_state errors
        request.session.clear()
        request.session["active"] = True

        # Generate the Google OAuth redirect URL
        redirect_response = await oauth.google.authorize_redirect(request, redirect_uri)
        login_url = redirect_response.headers["location"]

        # Return JSON-friendly format
        return {"google_login_url": login_url}

    @staticmethod
    async def handle_callback(request: Request, db: Session):
        """Step 2: Handle Google OAuth callback."""
        try:
            token = await oauth.google.authorize_access_token(request)
            user_info = await oauth.google.parse_id_token(request, token)

            if not user_info or "email" not in user_info:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Google login failed — no email found",
                )

            email = user_info["email"]
            name = user_info.get("name", "Google User")

            # 🔍 Check if user exists
            user = db.query(User).filter(User.email == email).first()
            if not user:
                # ✅ Create new user if doesn't exist
                user = User(email=email, full_name=name, is_verified=True, is_active=True)
                db.add(user)
                db.commit()
                db.refresh(user)

            # 🔑 Generate JWT token
            access_token = create_token(data={"id": user.id, "email": user.email})

            # ✅ HTML Response (for browser flow)
            html_content = f"""
            <html>
                <head><title>Google Login Success</title></head>
                <body style='font-family: Arial; text-align:center; margin-top:10%;'>
                    <h2>✅ Google Login Successful</h2>
                    <p>Welcome, <b>{email}</b></p>
                    <p>Your access token:</p>
                    <code>{access_token}</code>
                    <br><br>
                    <a href="/dashboard?token={access_token}">
                        <button style="padding:10px 20px; background:#007bff; color:white; border:none; border-radius:5px;">
                            Go to Dashboard
                        </button>
                    </a>
                </body>
            </html>
            """
            return HTMLResponse(content=html_content, status_code=200)

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"OAuth error: {str(e)}",
            )





# from fastapi import HTTPException, status, Request
# from starlette.responses import HTMLResponse
# from authlib.integrations.starlette_client import OAuth
# from sqlalchemy.orm import Session
# from models.auth_user import User
# from utils.auth_user import create_token
# from config.config import settings

# oauth = OAuth()
# oauth.register(
#     name="google",
#     client_id=settings.GOOGLE_CLIENT_ID,
#     client_secret=settings.GOOGLE_CLIENT_SECRET,
#     access_token_url="https://oauth2.googleapis.com/token",
#     authorize_url="https://accounts.google.com/o/oauth2/auth",
#     api_base_url="https://www.googleapis.com/oauth2/v2/",
#     client_kwargs={"scope": "openid email profile"},
# )

# class GoogleAuthQuery:
#     @staticmethod
#     async def get_login_url(request: Request):
#         redirect_uri = "http://localhost:8000/Oauth/auth/google/callback"

#         # ✅ Force new session each time to sync state
#         request.session.clear()
#         request.session["active"] = True

#         # Redirect to Google login
#         redirect_response = await oauth.google.authorize_redirect(request, redirect_uri)
#         login_url = str(redirect_response.headers["location"])
#         return {"google_login_url": login_url}

#     @staticmethod
#     async def callback(request: Request, db: Session):
#         try:
#             # ✅ Validate session still active
#             if not request.session.get("active"):
#                 raise HTTPException(status_code=400, detail="Session expired or invalid")

#             token = await oauth.google.authorize_access_token(request)
#             user_info = await oauth.google.parse_id_token(request, token)

#             if not user_info or "email" not in user_info:
#                 raise HTTPException(status_code=400, detail="Google login failed — no email found")

#             email = user_info["email"]
#             user = db.query(User).filter(User.email == email).first()

#             if not user:
#                 user = User(email=email, is_verified=True, is_active=True)
#                 db.add(user)
#                 db.commit()
#                 db.refresh(user)

#             access_token = create_token({"id": user.id})
#             request.session["user_email"] = email

#             html_content = f"""
#             <html>
#                 <head><title>Google Login Success</title></head>
#                 <body style='font-family: Arial; text-align:center; margin-top: 10%;'>
#                     <h2>✅ Google Login Successful</h2>
#                     <p>Welcome, <b>{email}</b></p>
#                     <p>Your access token:</p>
#                     <code>{access_token}</code>
#                     <br><br>
#                     <a href="/dashboard?token={access_token}">Go to Dashboard</a>
#                 </body>
#             </html>
#             """
#             return HTMLResponse(content=html_content, status_code=200)

#         except Exception as e:
#             raise HTTPException(
#                 status_code=500,
#                 detail=f"OAuth error: {str(e)}",
#             )









