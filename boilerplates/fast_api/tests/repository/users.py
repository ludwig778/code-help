from app.repository.users import create_new_user
from app.schemas import UserCreate


def test_create_user(db_session):
    user = create_new_user(
        db_session,
        UserCreate(
            username="test_user", email="test_user@example.com", password="test_password", is_active=True, is_superuser=False
        ),
    )

    assert user
