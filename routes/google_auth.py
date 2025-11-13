# routes/google_auth_routes.py
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from database import get_db
from repositories.google_auth import GoogleAuthQuery

router = APIRouter(prefix="/Oauth", tags=["Google OAuth"])

# ✅ Step 1: Get Google Login URL
@router.get("/auth/google")
async def google_login(request: Request):
    return await GoogleAuthQuery.get_login_url(request)

# ✅ Step 2: Handle Google Callback
@router.get("/auth/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    return await GoogleAuthQuery.handle_callback(request, db)
























# ✅ Step 2: Callback
# @router.get("/google/callback")
# async def google_callback(request: Request, db: Session = Depends(get_db)):
#     try:
#         token = await oauth.google.authorize_access_token(request)
#         user_info = await oauth.google.parse_id_token(request, token)
#         if not user_info:
#             return {"error": "Failed to retrieve user info"}

#         email = user_info.get("email")
#         name = user_info.get("name")

#         # ✅ Check or create user
#         user = db.query(User).filter(User.email == email).first()
#         if not user:
#             user = User(email=email, is_verified=True, login_provider="google")
#             db.add(user)
#             db.commit()
#             db.refresh(user)

#         # ✅ Create JWT tokens
#         access_token, refresh_token = create_tokens(user.id, user.email)

#         # ✅ Store in session for template access
#         request.session["user_email"] = user.email
#         request.session["access_token"] = access_token

#         # ✅ Redirect to dashboard page
#         return RedirectResponse(url="/dashboard")

#     except Exception as e:
#         return {"message": f"OAuth error: {str(e)}"}


