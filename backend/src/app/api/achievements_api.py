"""
Описание API для работы с достижениями
"""
from typing import List

from fastapi import APIRouter, Depends
from app.services.achievement_services import AchievementService
from app.models.achievement_models import (AchievementModel,
                                           AchievementCreationModel)
from app.tables import Achievements


router = APIRouter(
    prefix="/achievements",
    tags=["Achievements API"]
)


@router.get('/all/', response_model=List[AchievementModel])
def get_all_achievements(
    service: AchievementService = Depends()
) -> List[Achievements]:
    
    return service.get_all_achievements()


@router.post('/add/')
def add_new_achievement(
    achievement: AchievementCreationModel,
    service: AchievementService = Depends()
) -> dict:

    return service.add_new_achievement(
        achievement_name=achievement.achievement_name,
        achievement_value=achievement.achievement_value,
        achievement_desc=achievement.achievement_desc
    )
