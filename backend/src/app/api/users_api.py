"""
Описание API для работы с пользователями
"""
from datetime import date

from fastapi import APIRouter, Depends

from app.api import stats_api
from app.services.user_services import UserService
from app.models.user_models import UserModel
from app.models.achievement_models import AchievementModel
from app.tables import (Users,
                        Achievements)


router = APIRouter(
    prefix="/users",
    tags=["Users API"]
)

router.include_router(stats_api.router)


@router.get(
    '/{user_id}/',
    response_model=UserModel
)
def get_user(
    user_id: int,
    service: UserService = Depends()
) -> Users:
    """
    Метод API  для получения пользователя по id
    """
    return service.get_user(
        user_id=user_id
    )


@router.post(
    '/{user_id}/reward/{achievement_id}'
)
def reward_user_with_achievement(
    achievement_id: int,
    user_id: int,
    reward_date: date = date.today(),
    service: UserService = Depends()
) -> dict:
    """
    Метод API для присвоению пользователю достижения
    Args:
        achievement_id: int - id достижения
        user_id: int - id пользователя
        reward_date: date - дата достижения
    Returns:
        dict со статусом добавления
    """
    return service.reward_user_with_achievement(
        achievement_id=achievement_id,
        user_id=user_id,
        reward_date=reward_date
    )


@router.get(
    '/{user_id}/ahievements/',
    response_model=list[tuple[AchievementModel, date]]
)
def get_user_achievements(
    user_id: int,
    service: UserService = Depends()
) -> list[tuple[Achievements, date]]:
    """
    Метод API для получения всех достижения пользователя
    Args:
        user_id: int - id пользователя
    Returns:
        ist[tuple[Achievements, date]] - список достижений
        с датами их получения
    """
    return service.get_user_achievements(
        user_id=user_id
    )
