"""
Файл пакета API
"""
from fastapi import APIRouter
from app.api import (users_api,
                     achievements_api)

router = APIRouter()

router.include_router(users_api.router)
router.include_router(achievements_api.router)
