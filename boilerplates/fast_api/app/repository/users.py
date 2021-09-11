from typing import List, Optional

from sqlalchemy.orm import Session

from app.core.hashing import get_password_hash
from app.db.models import User
from app.schemas import UserCreate


def create_user(db: Session, user_data: UserCreate) -> User:
    user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password),
        is_active=user_data.is_active,
        is_superuser=user_data.is_superuser,
    )

    db.add(user)

    db.commit()
    db.refresh(user)

    return user


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    user = db.query(User).filter(User.username == username).first()

    return user


def list_users(db: Session) -> List[User]:
    return db.query(User).all()


def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
