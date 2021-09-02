from pytest import fixture

from app.main import get_app
from fastapi.testclient import TestClient
from app.db.models import Base
from app.db.session import session_factory, engine
from app.repository.users import create_new_user
from app.schemas import UserCreate


@fixture(scope="session")
def app():
    return get_app()


@fixture(scope="function")
def unauthorized_client(app):
    return TestClient(app)


@fixture(scope="function")
def admin_client(app):
    client = TestClient(app)

    response = client.post("/api/v1/login/", data={"username": "user_1", "password": "secret_1"})
    access_token = response.json().get("access_token")

    client.headers.update({"Authorization": f"Bearer {access_token}"})

    return client


@fixture(scope="function")
def client(app):
    client = TestClient(app)

    response = client.post("/api/v1/login/", data={"username": "user_2", "password": "secret_2"})
    access_token = response.json().get("access_token")

    client.headers.update({"Authorization": f"Bearer {access_token}"})

    return client


@fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)

    session = session_factory()

    yield session

    session.close()
    Base.metadata.drop_all(bind=engine)


@fixture(autouse=True, scope="function")
def seed_database(db_session):
    users = [
        {
            "id": 1,
            "username": "user_1",
            "email": "user_1@example.com",
            "password": "secret_1",
            "is_active": True,
            "is_superuser": True,
        },
        {
            "id": 2,
            "username": "user_2",
            "email": "user_2@example.com",
            "password": "secret_2",
            "is_active": True,
            "is_superuser": False,
        },
        {
            "id": 3,
            "username": "user_3",
            "email": "user_3@example.com",
            "password": "secret_3",
            "is_active": False,
            "is_superuser": False,
        },
    ]

    for user in users:
        create_new_user(db_session, UserCreate(**user))
