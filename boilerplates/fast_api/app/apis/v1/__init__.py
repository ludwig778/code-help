from fastapi import APIRouter

from app.apis.v1.login import router as router_login
from app.apis.v1.users import router as router_users

v1_router = APIRouter()

v1_router.include_router(router_login, prefix="/login", tags=["login"])
v1_router.include_router(router_users, prefix="/users", tags=["users"])
