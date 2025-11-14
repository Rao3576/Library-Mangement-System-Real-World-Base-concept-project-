from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from config.config import settings
from typing import List

# ✅ Security scheme
security = HTTPBearer()

# ✅ Extract current user role from JWT
def get_current_user_role(credentials=Depends(security)):
    token = credentials.credentials  # Extract raw token string

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        role = payload.get("role")
        if not role:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token missing role information",
            )
        return role

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

# ✅ Role-based access decorator
def require_role_in(roles: List[str]):
    def role_dependency(current_role: str = Depends(get_current_user_role)):
        if current_role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission denied: Requires one of {roles}",
            )
        return current_role
    return role_dependency







# from fastapi import Depends, HTTPException, status
# from typing import List
# from jose import jwt, JWTError
# from config.config import settings
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# # Bearer auth scheme
# oauth2_scheme = HTTPBearer()

# # Decode token and extract role
# def get_current_user_role(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
#     try:
#         # ✅ Extract actual JWT string from credentials
#         token = credentials.credentials  
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

#         role = payload.get("role")
#         if role is None:
#             raise HTTPException(
#                 status_code=status.HTTP_401_UNAUTHORIZED,
#                 detail="Role not found in token"
#             )
#         return role
#     except JWTError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or expired token"
#         )

# # Role-based restriction
# def require_role_in(roles: List[str]):
#     def wrapper(current_role: str = Depends(get_current_user_role)):
#         if current_role not in roles:
#             raise HTTPException(
#                 status_code=status.HTTP_403_FORBIDDEN,
#                 detail="Not enough permissions"
#             )
#         return current_role
#     return wrapper
