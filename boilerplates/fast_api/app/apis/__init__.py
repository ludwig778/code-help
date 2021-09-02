from fastapi import APIRouter
from app.apis.v1 import v1_router

root_router = APIRouter()

root_router.include_router(v1_router, prefix="/v1", tags=["api"])
