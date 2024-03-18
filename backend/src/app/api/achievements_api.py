"""
Описание API для работы с достижениями
"""
from fastapi import APIRouter, Depends
from app.services.achievement_services import AchievementService
from app.models.achievement_models import (AchievementModel,
                                           AchievementCreationModel)
from app.tables import Achievements


router = APIRouter(
    prefix="/achievements",
    tags=["Achievements API"]
)


@router.get('/all/', response_model=list[AchievementModel])
def get_all_achievements(
    service: AchievementService = Depends()
) -> list[Achievements]:
    """
    Метод APi для получения списка всех достижений
    """
    return service.get_all_achievements()


@router.post('/add/')
def add_new_achievement(
    achievement: AchievementCreationModel,
    service: AchievementService = Depends()
) -> dict:
    """
    Метод API для добавления нового достижения в
    базу данных
    Args:
        achievement: AchievementCreationModel - модель с данными нвого
        достижения
    Returns:
            dict - словарь со статусом добавления достижения
            в базу данных
    """
    return service.add_new_achievement(
        achievement_name=achievement.achievement_name,
        achievement_value=achievement.achievement_value,
        achievement_desc=achievement.achievement_desc
    )
