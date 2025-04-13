from fastapi_users import FastAPIUsers
from fastapi import APIRouter

from users.schemas import UserCreate, UserRead
from users.user_manager import get_user_manager
from users.models import User
from users.auth_backend import authentication_backend

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [authentication_backend],
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)






