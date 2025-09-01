from fastapi import APIRouter, Depends, HTTPException
from utils import decode_jwt_token
from database import users_collection

user_router = APIRouter()

def get_current_user(token: str = Depends(decode_jwt_token)):
    payload = decode_jwt_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload

@user_router.get("/me")
async def get_me(user: dict = Depends(get_current_user)):
    return {"email": user["email"]}
