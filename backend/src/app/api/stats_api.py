"""
Описание API для работы со статистикой
"""
from typing import List, Tuple

from fastapi import APIRouter, Depends
from app.services.user_services import UserService
from app.models.user_models import UserModel
from app.tables import Users


router = APIRouter(
    prefix="/stats"
)


@router.get(
    '/most_achievements/',
    response_model=List[Tuple[UserModel, int]]
)
def get_user_with_most_achievements(
    service: UserService = Depends()
) -> List[Tuple[Users, int]]:

    return service.get_users_with_most_achievements()


@router.get(
    '/max_score/',
    response_model=List[Tuple[UserModel, int]]
)
def get_user_with_max_score(
    service: UserService = Depends()
) -> List[Tuple[Users, int]]:

    return service.get_users_with_max_score()


@router.get(
    '/max_gap/',
    response_model=List[Tuple[UserModel, UserModel, int]]
)
def get_users_with_max_gap(
    service: UserService = Depends()
) -> list[Tuple[UserModel, UserModel, int]]:
    
    return service.get_users_with_max_gap()


@router.get(
    '/min_gap/',
    response_model=List[Tuple[UserModel, UserModel, int]]
)
def get_users_with_min_gap(
    service: UserService = Depends()
) -> list[Tuple[UserModel, UserModel, int]]:
    
    return service.get_users_with_min_gap()


@router.get(
    '/with_7_streak/',
    response_model=List[UserModel]
)
def get_users_with_7_days_streak(
    service: UserService = Depends()
) -> List[Users]:
    
    return service.get_users_with_7_days_streak()
