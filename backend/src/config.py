from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    BACKEND_PORT: int
    CORS: str
    TOKEN_LIFETIME: int
    RESET_TOKEN_SECRET: str
    VERIFICATION_TOKEN_SECRET: str
    
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASS: str
    
    FRONTEND_PORT: int
    BACKEND_API: str

    @property
    def POSTGRES_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def POSTGRES_URL_psycopg(self):
        return f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASS}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file="././.env")

settings = Settings()