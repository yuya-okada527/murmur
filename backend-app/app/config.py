from pydantic import BaseSettings


class Settings(BaseSettings):
    db_engine: str = "postgresql"
    db_user: str
    db_password: str
    db_host: str = "localhost"
    db_port: int = 54321
    db_name: str = "murmur"

    class Config:
        env_file = ".env"


settings = Settings()
