"""
Описание API для работы с пользователями
"""
from datetime import date
from typing import List, Tuple

from fastapi import APIRouter, Depends

import app.api.stats_api as stats_api
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
    
    return service.get_user(
        user_id=user_id
    )


@router.post(
    '/{user_id}/reward/{achievement_id}'
)
def reward_user_with_achievement(
    achievement_id: int,
    user_id: int,
    date: date = date.today(),
    service: UserService = Depends()
) -> dict:
    
    return service.reward_user_with_achievement(
        achievement_id=achievement_id,
        user_id=user_id,
        date=date
    )


@router.get(
    '/{user_id}/ahievements/',
    response_model=List[Tuple[AchievementModel, date]]
)
def get_user_achievements(
    user_id: int,
    service: UserService = Depends()
) -> List[Tuple[Achievements, date]]:

    return service.get_user_achievements(
        user_id=user_id
    )
