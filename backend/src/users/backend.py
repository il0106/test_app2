from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy
from src.users.strategy import get_database_strategy
from src.users.transport import cookie_transport


authentication_backend = AuthenticationBackend(
    name="cookie_plus_db",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)