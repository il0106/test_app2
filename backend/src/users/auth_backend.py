from fastapi_users.authentication import AuthenticationBackend
from users.strategy import get_database_strategy
from users.transport import cookie_transport


authentication_backend = AuthenticationBackend(
    name="cookie_plus_db",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)