from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    BACKEND_PORT: int
    CORS: str
    TOKEN_LIFETIME: int
    RESET_TOKEN_SECRET: str
    VERIFICATION_TOKEN_SECRET: str
    JWT_SECRET: str
    
    FRONTEND_PORT: int
    BACKEND_API: str

    model_config = SettingsConfigDict(env_file="../.env")

settings = Settings()