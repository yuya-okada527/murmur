from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

DB_URL = f"{settings.db_engine}://" \
    f"{settings.db_user}:{settings.db_password}" \
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
