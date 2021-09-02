from fastapi import APIRouter

from app.apis.v1.users import router as router_users
from app.apis.v1.login import router as router_login
from app.apis.v1.hello import router as router_hello


v1_router = APIRouter()

v1_router.include_router(router_login, prefix="/login", tags=["login"])
v1_router.include_router(router_users, prefix="/users", tags=["users"])
v1_router.include_router(router_hello, prefix="/hello", tags=["hello"])
