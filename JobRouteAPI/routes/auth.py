from fastapi import APIRouter, HTTPException, Depends
from models import User
from database import users_collection
from utils import hash_password, create_jwt_token, verify_password
from pydantic import BaseModel

auth_router = APIRouter()

class RegisterUser(BaseModel):
    name: str
    email: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

@auth_router.post("/register")
async def register(user: RegisterUser):
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    user_dict = {
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }
    users_collection.insert_one(user_dict)
    return {"message": "User registered successfully"}

@auth_router.post("/login")
async def login(user: LoginUser):
    existing_user = users_collection.find_one({"email": user.email})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, existing_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid password")

    token = create_jwt_token({"email": user.email})
    return {"token": token, "token_type": "bearer"}
