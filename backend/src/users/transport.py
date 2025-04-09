from fastapi_users.authentication import CookieTransport

cookie_transport = CookieTransport(cookie_name='hi_cookie', cookie_max_age=3600*24)