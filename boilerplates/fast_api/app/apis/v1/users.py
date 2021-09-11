from fastapi import APIRouter, Depends

from app.core.security import get_current_active_user
from app.db.models import User
from app.schemas import User as UserModel

router = APIRouter()


@router.get("/me/", response_model=UserModel)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user.__dict__
