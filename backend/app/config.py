# backend/app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Task Manager AI"
    API_V1_STR: str = "/api/v1"
    CORS_ORIGINS: list = ["http://localhost:3000"]

settings = Settings()