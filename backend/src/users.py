import uuid
from typing import Optional
from datetime import datetime, timezone
import logging

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

# Настройка логирования
logger = logging.getLogger(__name__)

SECRET = settings['JWT_SECRET']
TOKEN_LIFETIME = int(settings['TOKEN_LIFETIME'])

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings['RESET_PASSWORD_TOKEN_SECRET']
    verification_token_secret = settings['VERIFICATION_TOKEN_SECRET']
    TOKEN_LIFETIME = TOKEN_LIFETIME

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        logger.info(f"User {user.id} has registered.")
        
        # Отправляем email для верификации при регистрации
        # if request:
        #     base_url = str(request.base_url).rstrip('/')
        #     await self.send_verification_email(user, base_url)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        logger.info(f"User {user.id} has forgot their password. Reset token: {token}")
        # Отправляем email для сброса пароля
        if request:
            base_url = str(request.base_url).rstrip('/')
            await email_service.send_password_reset_email(user.email, token, base_url)

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        logger.info(f"Verification requested for user {user.id}. Verification token: {token}")
        # Отправляем email для верификации используя готовый токен
        if request:
            base_url = str(request.base_url).rstrip('/')
            await email_service.send_verification_email(user.email, token, base_url)

    async def send_verification_email(self, user: User, base_url: str):
        """Отправляет email для верификации пользователя"""
        try:
            # Создаем токен верификации используя правильный метод
            token_data = {"sub": str(user.id), "email": user.email, "aud": "fastapi-users:verify"}
            token = generate_jwt(token_data, self.verification_token_secret, TOKEN_LIFETIME)
            logger.info(f"Generated verification token for user {user.id}")
            await email_service.send_verification_email(user.email, token, base_url)
        except Exception as e:
            logger.error(f"Error sending verification email to user {user.id}: {e}")
            raise

    async def verify_user(self, token: str) -> Optional[User]:
        """Верифицирует пользователя по токену"""
        try:
            logger.info(f"Attempting to verify user with token: {token[:20]}...")
            
            # Декодируем токен
            token_data = decode_jwt(token, 
                                    self.verification_token_secret, 
                                    ["fastapi-users:verify"])
            logger.info(f"Token decoded successfully: {token_data}")
            
            # Получаем ID пользователя
            user_id = uuid.UUID(token_data["sub"])
            logger.info(f"User ID from token: {user_id}")
            
            # Получаем пользователя из базы данных
            user = await self.get(user_id)
            if not user:
                logger.error(f"User with ID {user_id} not found")
                return None
                
            logger.info(f"User found: {user.email}, is_verified: {user.is_verified}")
            
            # Проверяем, не верифицирован ли уже пользователь
            if user.is_verified:
                logger.info(f"User {user.id} is already verified")
                return user
            
            # Верифицируем пользователя
            user.is_verified = True
            user.verified_at = datetime.now(timezone.utc)
            await self.user_db.update(user, {"is_verified": True, "verified_at": user.verified_at})
            
            logger.info(f"User {user.id} successfully verified")
            return user
            
        except Exception as e:
            logger.error(f"Error verifying user: {e}", exc_info=True)
            return None


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    return UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=TOKEN_LIFETIME)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)