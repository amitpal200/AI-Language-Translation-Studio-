import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", f"sqlite:///{BASE_DIR / 'database' / 'translator.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DOWNLOAD_FOLDER = BASE_DIR / "downloads"
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024
