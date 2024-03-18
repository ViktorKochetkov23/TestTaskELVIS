from enum import Enum

from pydantic import BaseModel, ConfigDict


class LanguageSetting(Enum):
    RU = 'ru'
    EN = 'en'


class UserModel(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    user_name: str
    language: LanguageSetting
