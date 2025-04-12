import logging
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin

from users.models import User
from users.utils import get_user_db
from config import settings

log = logging.getLogger(__name__)
# class IdIntPkMixin:
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = settings.RESET_TOKEN_SECRET
    verification_token_secret = settings.VERIFICATION_TOKEN_SECRET


    async def on_after_register(self, user: User, request: Optional[Request] = None):
        log.warning("User %r has registered.", user.id)


    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        
        log.warning("Verification requested for user %r. Verification token: %r", user.id, token)


    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning("User %r has forgot their password. Reset token: %r", user.id, token)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)