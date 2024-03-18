"""
Сервисы для API для работы с достижениями
"""
from sqlalchemy.sql.expression import (select,
                                       insert)

from app.tables import Achievements
from app.services.base_services import UpdateBaseService


class AchievementService(UpdateBaseService):
    """Класс инкапсулирует логику работы с достижениями"""
    def get_all_achievements(
        self
    ) -> list[Achievements]:
        """Метод возвращает все достижения в базе данных"""
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
        """
        Метод добавляет новое достижение в базу данных
        Args:
            achievement_name: str - имя достижения
            achievement_value: int - очки за достижения
            achievement_desc: str - описание достижения
        Returns:
            dict - словарь со статусом добавления достижения
            в базу данных
        """
        statement = insert(Achievements).values(
            achievement_name=achievement_name,
            achievement_value=achievement_value,
            achievement_desc=achievement_desc
        )

        return self.execute_update_statement(statement)
