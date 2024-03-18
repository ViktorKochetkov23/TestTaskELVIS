"""
Описание API для работы со статистикой
"""
from fastapi import APIRouter, Depends

from app.services.user_services import UserService
from app.models.user_models import UserModel
from app.tables import Users


router = APIRouter(
    prefix="/stats"
)


@router.get(
    '/most_achievements/',
    response_model=list[tuple[UserModel, int]]
)
def get_user_with_most_achievements(
    service: UserService = Depends()
) -> list[tuple[Users, int]]:
    """
    Метод API для получения пользователей с самым
    большим количеством достижений
    Args:
        -
    Returns:
        list[tuple[Users, int]] - список пользователей с количествами
        их достижений
    """
    return service.get_users_with_most_achievements()


@router.get(
    '/max_score/',
    response_model=list[tuple[UserModel, int]]
)
def get_user_with_max_score(
    service: UserService = Depends()
) -> list[tuple[Users, int]]:
    """
    Метод API для получения пользователей с самым большим количеством
    очков достижений
    Args:
        -
    Returns:
        list[tuple[Users, int]] - список пользователей с их очками
    """
    return service.get_users_with_max_score()


@router.get(
    '/max_gap/',
    response_model=list[tuple[UserModel, UserModel, int]]
)
def get_users_with_max_gap(
    service: UserService = Depends()
) -> list[tuple[Users, Users, int]]:
    """
    Метод API для получения пользователей с самой большой разностью
    очков достижений
    Args:
        -
    Returns:
        list[tuple[Users, Users, int]] - список с парами пользователей
        и разностью их очков
    """
    return service.get_users_with_max_gap()


@router.get(
    '/min_gap/',
    response_model=list[tuple[UserModel, UserModel, int]]
)
def get_users_with_min_gap(
    service: UserService = Depends()
) -> list[tuple[UserModel, UserModel, int]]:
    """
    Метод API для получения пользователей с самой большой разностью
    очков достижений
    Args:
        -
    Returns:
        list[tuple[Users, Users, int]] - список с парами пользователей
        и разностью их очков
    """
    return service.get_users_with_min_gap()


@router.get(
    '/with_7_streak/',
    response_model=list[UserModel]
)
def get_users_with_7_days_streak(
    service: UserService = Depends()
) -> list[Users]:
    """
    Метод API для получения пользователей, которые когда-либо
    получали достижения 7 дней подряд
    Args:
        -
    Returns:
        list[Users] - списко объектов пользователей
    """
    return service.get_users_with_7_days_streak()
