from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn 
from contextlib import asynccontextmanager
import asyncio

from config import settings
from users import (
    engine, 
    Base,
    fastapi_users,
    User,
    UserCreate,
    UserRead,
    UserUpdate,
    auth_backend,
    get_user_manager
)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup
#     async with engine.begin() as conn:
#         # Drop all tables first
#         await conn.run_sync(Base.metadata.drop_all)
#         # Create all tables
#         await conn.run_sync(Base.metadata.create_all)
#     yield
#     # Shutdown
#     await engine.dispose()

app = FastAPI(#lifespan=lifespan
    )

# Include user management routes
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# Разрешаем CORS для фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", 
                   "http://localhost:8080", 
                   "http://127.0.0.1:3000", 
                   "http://127.0.0.1:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sum")
def read_sum(a: float, b: float):
    return {"sum": a + b}

@app.get("/settings")
def read_config():
    return {str(settings)}

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.BACKEND_PORT, reload=True)