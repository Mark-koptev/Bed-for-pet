from pydantic_settings import BaseSettings
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = f"{BASE_DIR}/.env"


settings = Settings()
print(settings.DATABASE_URL)
