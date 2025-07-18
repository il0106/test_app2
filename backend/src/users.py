import uuid
from typing import Optional
from datetime import datetime

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.jwt import generate_jwt, decode_jwt

from src.db import User, get_user_db
from src.email_service import email_service

from config import settings

SECRET = settings['JWT_SECRET']


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings['RESET_PASSWORD_TOKEN_SECRET']
    verification_token_secret = settings['VERIFICATION_TOKEN_SECRET']

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        # Отправляем email для верификации при регистрации
        if request:
            base_url = str(request.base_url).rstrip('/')
            await self.send_verification_email(user, base_url)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")
        # Отправляем email для сброса пароля
        if request:
            base_url = str(request.base_url).rstrip('/')
            await email_service.send_password_reset_email(user.email, token, base_url)

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
        # Отправляем email для верификации
        if request:
            base_url = str(request.base_url).rstrip('/')
            await email_service.send_verification_email(user.email, token, base_url)

    async def send_verification_email(self, user: User, base_url: str):
        """Отправляет email для верификации пользователя"""
        # Создаем токен верификации используя правильный метод
        token_data = {"sub": str(user.id), "email": user.email, "aud": "fastapi-users:verify"}
        token = generate_jwt(token_data, self.verification_token_secret, 3600)  # 1 hour
        await email_service.send_verification_email(user.email, token, base_url)

    async def verify_user(self, token: str) -> Optional[User]:
        """Верифицирует пользователя по токену"""
        try:
            token_data = decode_jwt(token, 
                                    self.verification_token_secret, 
                                    ["fastapi-users:verify"])
            user_id = uuid.UUID(token_data["sub"])
            user = await self.get(user_id)
            if user and not user.is_verified:
                user.is_verified = True
                user.verified_at = datetime.utcnow()
                await self.user_db.update(user)
                return user
        except Exception as e:
            print(f"Error verifying user: {e}")
        return None


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
