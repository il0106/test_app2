from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.db import User, create_db_and_tables
from src.schemas import UserCreate, UserRead, UserUpdate, VerificationResponse, ResendVerificationRequest
from src.users import auth_backend, current_active_user, fastapi_users, get_user_manager, UserManager
from src.email_service import email_service
from config import settings


async def lifespan(app: FastAPI):
    # Startup
    await create_db_and_tables()
    yield
    # Shutdown
    pass


app = FastAPI(lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings["ALLOWED_ORIGINS"].split(","), 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.get("/verify-email/{token}")
async def verify_email(token: str, request: Request, user_manager: UserManager = Depends(get_user_manager)):
    """
    Верифицирует email пользователя по токену
    """
    user = await user_manager.verify_user(token)
    
    if user:
        return {"success": True, "message": "Email успешно верифицирован"}
    else:
        raise HTTPException(status_code=400, detail="Недействительный токен верификации")


@app.post("/resend-verification", response_model=VerificationResponse)
async def resend_verification(request: ResendVerificationRequest, req: Request, user_manager: UserManager = Depends(get_user_manager)):
    """
    Повторно отправляет email для верификации
    """
    try:
        # Находим пользователя по email
        user = await user_manager.get_by_email(request.email)
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        
        if user.is_verified:
            return VerificationResponse(
                success=False,
                message="Email уже верифицирован"
            )
        
        # Отправляем новый email для верификации
        base_url = str(req.base_url).rstrip('/')
        await user_manager.send_verification_email(user, base_url)
        
        return VerificationResponse(
            success=True,
            message="Email для верификации отправлен"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка отправки email: {str(e)}")


@app.get("/user/verification-status")
async def get_verification_status(user: User = Depends(current_active_user)):
    """
    Возвращает статус верификации текущего пользователя
    """
    return {
        "is_verified": user.is_verified,
        "verified_at": user.verified_at,
        "created_at": user.created_at
    }
