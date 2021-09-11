from copy import deepcopy

from fastapi.testclient import TestClient
from pytest import fixture

from app.core.hashing import get_password_hash
from app.db.models import Base, User
from app.db.session import Session, engine, get_db
from app.main import get_app


@fixture(scope="function")
def setup_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    yield

    Base.metadata.drop_all(engine)


@fixture(scope="function")
def db_session():
    with Session() as session:
        yield session


@fixture(scope="function")
def app(setup_database, db_session):
    app = get_app()

    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    yield app


@fixture(scope="function")
def unauthorized_client(app):
    return TestClient(app)


def login(client, username, password):
    response = client.post(
        "/api/v1/login/", data={"username": username, "password": password}
    )
    access_token = response.json().get("access_token")

    client.headers.update({"Authorization": f"Bearer {access_token}"})

    return client


@fixture(scope="function")
def admin_client(app):
    client = login(TestClient(app), "user_1", "secret_1")

    return client


@fixture(scope="function")
def client(app):
    client = login(TestClient(app), "user_2", "secret_2")

    return client


@fixture(scope="session")
def users():
    return [
        User(
            username="user_1",
            email="user_1@example.com",
            hashed_password=get_password_hash("secret_1"),
            is_active=True,
            is_superuser=True,
        ),
        User(
            username="user_2",
            email="user_2@example.com",
            hashed_password=get_password_hash("secret_2"),
            is_active=True,
            is_superuser=False,
        ),
        User(
            username="user_3",
            email="user_3@example.com",
            hashed_password=get_password_hash("secret_3"),
            is_active=False,
            is_superuser=False,
        ),
    ]


@fixture(autouse=True, scope="function")
def seed_database(setup_database, db_session, users):

    db_session.add_all(deepcopy(users))
    db_session.commit()

    yield
