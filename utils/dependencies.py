from fastapi import Depends, HTTPException, status
from typing import List
from jose import jwt, JWTError
from config.config import settings
from fastapi.security import HTTPBearer

oauth2_scheme = HTTPBearer()

# Decode token and extract role
def get_current_user_role(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        role = payload.get("role")
        if role is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid role in token")
        return role
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

# Role-based restriction
def require_role_in(roles: List[str]):
    def wrapper(current_role: str = Depends(get_current_user_role)):
        if current_role not in roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
        return current_role
    return wrapper
