from pydantic_settings import BaseSettings
from typing import List
import secrets

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI Project"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost", "http://localhost:4200", "http://localhost:3000"]
    
    # Database settings
    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str
    DB_PREFIX: str
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 