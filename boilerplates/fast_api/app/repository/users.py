from sqlalchemy.orm import Session

from app.core.hashing import get_password_hash
from app.db.models import User
from app.schemas import UserCreate, UserInDB


def create_new_user(db: Session, user: UserCreate):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_active=user.is_active,
        is_superuser=user.is_superuser,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()

    if user:
        return UserInDB(**user.__dict__)
