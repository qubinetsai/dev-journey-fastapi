import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "FastAPI Hello World"
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")


settings = Settings()
