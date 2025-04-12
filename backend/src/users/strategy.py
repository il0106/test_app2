from typing import TYPE_CHECKING
from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy

from users.utils import get_access_token_db
from config import settings

if TYPE_CHECKING:
    from src.users.models import AccessToken


def get_database_strategy(
    access_token_db: AccessTokenDatabase["AccessToken"] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=settings.TOKEN_LIFETIME)


