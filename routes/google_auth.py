from fastapi import APIRouter, Request, Depends, Query, Header
from sqlalchemy.orm import Session
from database import get_db
from repositories.google_auth import GoogleOAuthQuery

router = APIRouter(prefix="/Oauth", tags=["OAuth2 & JWT"])

# ✅ Redirect to Google
@router.get("/auth/google")
async def google_login(request: Request):
    return await GoogleOAuthQuery.google_login(request)

# ✅ Google OAuth callback
@router.get("/auth/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    return await GoogleOAuthQuery.google_callback(request, db)

# ✅ Refresh Token
@router.post("/refresh-token")
async def refresh_access_token(refresh_token: str = Query(...), db: Session = Depends(get_db)):
    return await GoogleOAuthQuery.refresh_access_token(refresh_token, db)

# ✅ Logout and blacklist tokens
@router.post("/logout")
async def logout_user(authorization: str = Header(None), db: Session = Depends(get_db)):
    if not authorization or not authorization.startswith("Bearer "):
        return {"message": "Authorization header missing"}
    token = authorization.split(" ")[1]
    return await GoogleOAuthQuery.logout_user(token, db)

