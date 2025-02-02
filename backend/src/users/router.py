from fastapi import APIRouter, HTTPException, Response, status
from src.users.dao import UsersDAO
from src.users.schemas import SUserAuth
from src.users.auth import authenticate_user, create_access_token, get_password_hash


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)


@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("app_access_token", access_token,httponly=True)
    return {"access_token":access_token}