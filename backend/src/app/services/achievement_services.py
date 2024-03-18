"""
Сервисы для API для работы с достижениями
"""
from typing import List

from sqlalchemy.sql.expression import (select,
                                       insert)

from app.tables import (Achievements,
                        UsersAchievements)
from app.services.base_services import UpdateBaseService


class AchievementService(UpdateBaseService):

    
    def get_all_achievements(
        self
    ) -> List[Achievements]:

        statement = select(Achievements)
        sqlalchemy_result = self.session.execute(statement).all()
        result = [row[0] for row in sqlalchemy_result]
        return result
    

    def add_new_achievement(
        self,
        achievement_name: str,
        achievement_value: int,
        achievement_desc: str
    ) -> dict:
        
        statement = insert(Achievements).values(
            achievement_name=achievement_name,
            achievement_value=achievement_value,
            achievement_desc=achievement_desc
        )

        return self.execute_update_statement(statement)
