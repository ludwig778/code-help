from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings

engine = create_engine(settings.postgres_url)

Session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db() -> Generator:
    with Session() as session:
        yield session
