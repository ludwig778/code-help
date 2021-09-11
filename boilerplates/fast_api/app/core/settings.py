from os import environ


class Settings:
    SECRET_KEY: str = environ["SECRET_KEY"]
    ALGORITHM: str = environ.get("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
    )

    POSTGRES_HOST: str = environ["POSTGRES_HOST"]
    POSTGRES_USER: str = environ["POSTGRES_USER"]
    POSTGRES_PASSWORD: str = environ["POSTGRES_PASSWORD"]
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", 5432))
    POSTGRES_DB: str = environ.get("POSTGRES_DB", POSTGRES_USER)

    @property
    def postgres_url(cls):
        return (
            f"postgresql://{cls.POSTGRES_USER}:{cls.POSTGRES_PASSWORD}"
            f"@{cls.POSTGRES_HOST}:{cls.POSTGRES_PORT}/"
            f"{cls.POSTGRES_DB}"
        )


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

settings = Settings()
