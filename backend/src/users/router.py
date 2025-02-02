from fastapi import APIRouter, HTTPException
from dao import UsersDAO
from schemas import UserRegister

router = APIRouter()

@router.post('/register')
async def register_user(user_data: UserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")