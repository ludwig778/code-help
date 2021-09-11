from app.repository.users import (
    create_user,
    delete_user,
    get_user_by_username,
    list_users,
)
from app.schemas import UserCreate


def test_create_user(db_session):
    assert create_user(
        db_session,
        UserCreate(
            username="test_user",
            email="test_user@example.com",
            password="test_password",
            is_active=True,
            is_superuser=False,
        ),
    )


def test_get_user(db_session):
    assert get_user_by_username(db_session, "user_1")


def test_get_non_existing_user(db_session):
    assert not get_user_by_username(db_session, "no_user")


def test_list_user(db_session):
    assert len(list_users(db_session)) == 3


def test_delete_user(db_session):
    user = get_user_by_username(db_session, "user_1")

    delete_user(db_session, user)

    assert len(list_users(db_session)) == 2
