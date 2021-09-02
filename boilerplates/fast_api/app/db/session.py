from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from app.core.settings import settings

engine = create_engine(settings.postgres_url)  # , echo=True)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = session_factory()
        yield db
    finally:
        db.close()
