"""
Модуль с моделями для представления данных о пользователях
"""
from enum import Enum

from pydantic import BaseModel, ConfigDict


class LanguageSetting(Enum):
    """
    Класс языковых настроек пользователей
    """
    RU = 'ru'
    EN = 'en'


class UserModel(BaseModel):
    """
    Модель для представления данных пользователя
    """
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_name: str
    language: LanguageSetting
