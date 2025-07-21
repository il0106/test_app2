import uuid
from datetime import datetime
from typing import Optional

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[uuid.UUID]):
    is_verified: bool
    verified_at: Optional[datetime] = None
    created_at: datetime
    is_customer: bool


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class VerificationResponse(BaseModel):
    success: bool
    message: str


class ResendVerificationRequest(BaseModel):
    email: str
