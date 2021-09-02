from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.apis import root_router
from app.core.settings import origins


def get_app():
    app = FastAPI()

    app.include_router(root_router, prefix="/api", tags=["api"])

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
