import datetime

from pydantic import BaseModel, ConfigDict, Field


class AchievementModel(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int
    achievement_name: str
    achievement_value: int
    achievement_desc: str


class AchievementCreationModel(BaseModel):
    
    achievement_name: str = Field(max_length=50)
    achievement_value: int
    achievement_desc: str = Field(max_length=150)
