from fastapi_users.authentication import CookieTransport

cookie_transport = CookieTransport(cookie_name='illy_cookie', cookie_max_age=3600*24)