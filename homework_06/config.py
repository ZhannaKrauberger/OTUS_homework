from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE_PATH = BASE_DIR / "my_wishlists.db"


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_FILE_PATH}"
    SQLALCHEMY_ECHO = False
    SECRET_KEY = "79596f591a0eaafc5e2433166e29ea02889d0e7ad1cc4b99e7d62ab6e9b29dc6"


class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
