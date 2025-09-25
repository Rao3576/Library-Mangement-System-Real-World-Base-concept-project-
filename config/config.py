from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER:Optional[str]
    DB_PASSWORD:Optional[str]
    DB_HOST:Optional[str]
    DB_PORT:Optional[int]
    DB_NAME:Optional[str]
    DB_CONNECTION:Optional[str]

    class Config:
        env_file = ".env"

    
settings = Settings()
