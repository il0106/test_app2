from fastapi import APIRouter, HTTPException
from src.users.dao import UsersDAO
from src.users.schemas import SUserRegister
from src.users.auth import get_password_hash

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)

@router.post('/register')
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)