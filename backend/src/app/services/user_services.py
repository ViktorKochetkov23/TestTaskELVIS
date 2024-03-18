"""
Сервисы для API для работы с пользователями
"""
from datetime import date, timedelta

from sqlalchemy import desc, case
import sqlalchemy.sql.functions as func
from sqlalchemy.sql.expression import (select,
                                       insert,
                                       column)
from googletrans import Translator

from app.tables import (Users,
                        Achievements,
                        UsersAchievements)
from app.services.base_services import UpdateBaseService


class UserService(UpdateBaseService):
    """Класс инкапсулирует логику работы с пользователями"""
    def get_user(
        self,
        user_id: int
    ) -> Users:
        """
        Метод возвращает пользователя по id
        Args:
            user_id: int - id пользователя
        Returns:
            Users - объект пользователя
        """
        print(self.session.get(Users, user_id))
        return self.session.get(Users, user_id)

    def reward_user_with_achievement(
        self,
        achievement_id: int,
        user_id: int,
        reward_date: date,
    ) -> dict:
        """
        Метод присваивает пользователю достижение
        Args:
            achievement_id: int - id достижения
            user_id: int - id пользователся
            reward_date: date - дата достижения
        Returns:
            dict со статусом добавления
        """
        inner_select = select(
            Users.id,
            Achievements.id,
            column(text=f"'{reward_date}'", is_literal=True)
        ).where(
            Users.id == user_id,
            Achievements.id == achievement_id
        )

        statement = insert(UsersAchievements).from_select(
            ['user_id', 'achievement_id', 'date'],
            inner_select
        )

        return self.execute_update_statement(statement)

    def get_user_achievements(
        self,
        user_id: int
    ) -> list[tuple[Achievements, date]]:
        """
        Метод возвращает все достижения пользователя
        Args:
            user_id: int - id пользователя
        Returns:
            ist[tuple[Achievements, date]] - список достижений
            с датами их получения
        """
        user = self.session.get(Users, user_id)
        langauge = user.language

        statement = select(
            Achievements,
            UsersAchievements.c.get('date')
        ).join(
            UsersAchievements,
            Achievements.id == UsersAchievements.c.get('achievement_id')
        ).where(
            UsersAchievements.c.get('user_id') == user_id
        )

        result = self.session.execute(statement).all()

        translator = Translator()

        for achievement, _ in result:
            achievement.achievement_name = translator.translate(
                achievement.achievement_name,
                dest=langauge
            ).text
            achievement.achievement_desc = translator.translate(
                achievement.achievement_desc,
                dest=langauge
            ).text

        return result

    def get_users_with_most_achievements(
        self
    ) -> list[tuple[Users, int]]:
        """
        Метод возвращает пользователей с самым большим
        количеством достижений
        Args:
            -
        Returns:
            list[tuple[Users, int]] - список с пользователями
            и количествами их достижения
        """
        achievements_column = case(
            (UsersAchievements.c.get('user_id') is None, 0),
            else_=func.count()
        ).label('Achievements')

        find_most_achievements = select(
            Users.id,
            UsersAchievements.c.get('user_id'),
            achievements_column
        ).join(
            UsersAchievements,
            UsersAchievements.c.get('user_id') == Users.id,
            isouter=True
        ).group_by(
            Users.id,
            UsersAchievements.c.get('user_id')
        ).order_by(
            desc('Achievements')
        ).limit(
            limit=1
        )

        most_achievements = self.session.execute(
            find_most_achievements
        ).one()[2]

        statement = select(
            Users,
            UsersAchievements.c.get('user_id'),
            achievements_column
        ).join(
            UsersAchievements,
            UsersAchievements.c.get('user_id') == Users.id,
            isouter=True
        ).group_by(
            Users.id,
            UsersAchievements.c.get('user_id')
        ).having(
            achievements_column == most_achievements
        )

        sqlalchemy_result = self.session.execute(statement).all()

        result = []
        for user, _, achievements in sqlalchemy_result:
            result.append((user, achievements))
        return result

    def get_users_with_max_score(
        self
    ) -> list[tuple[Users, int]]:
        """
        Метод возвращает пользователей с самыми большими
        очками достижений
        Args:
            -
        Returns:
            list[tuple[Users, int]] - списко с пользователями
            и их очками
        """
        score_column = func.sum(
            case(
                (Achievements.achievement_value is None, 0),
                else_=Achievements.achievement_value
            )
        ).label('Score')
        find_max_score = select(
            Users.id,
            score_column
        ).join(
            UsersAchievements,
            UsersAchievements.c.get('user_id') == Users.id,
            isouter=True
        ).join(
            Achievements,
            UsersAchievements.c.get('achievement_id') == Achievements.id,
            isouter=True
        ).group_by(
            Users.id
        ).order_by(
            desc('Score')
        ).limit(
            limit=1
        )

        max_score = self.session.execute(find_max_score).one()[1]

        statement = select(
            Users,
            score_column
        ).join(
            UsersAchievements,
            UsersAchievements.c.get('user_id') == Users.id,
            isouter=True
        ).join(
            Achievements,
            UsersAchievements.c.get('achievement_id') == Achievements.id,
            isouter=True
        ).group_by(
            Users.id
        ).having(
            score_column == max_score
        )

        result = self.session.execute(statement).all()

        return result

    def get_users_with_min_score(
        self
    ) -> list[tuple[Users, int]]:
        """
        Метод возвращает пользователей с самыми маленькими
        очками достижений
        Args:
            -
        Returns:
            list[tuple[Users, int]] - списко с пользователями
            и их очками
        """
        score_column = func.sum(
            case(
                (Achievements.achievement_value is None, 0),
                else_=Achievements.achievement_value
            )
        ).label('Score')
        find_min_score = select(
            Users.id,
            score_column
        ).join(
            UsersAchievements,
            UsersAchievements.c.get('user_id') == Users.id,
            isouter=True
        ).join(
            Achievements,
            UsersAchievements.c.get('achievement_id') == Achievements.id,
            isouter=True
        ).group_by(
            Users.id
        ).order_by(
            'Score'
        ).limit(
            limit=1
        )

        min_score = self.session.execute(find_min_score).one()[1]

        statement = select(
            Users,
            score_column
        ).join(
            UsersAchievements,
            UsersAchievements.c.get('user_id') == Users.id,
            isouter=True
        ).join(
            Achievements,
            UsersAchievements.c.get('achievement_id') == Achievements.id,
            isouter=True
        ).group_by(
            Users.id
        ).having(
            score_column == min_score
        )

        result = self.session.execute(statement).all()

        return result

    def get_users_with_max_gap(
        self
    ) -> list[tuple[Users, Users, int]]:
        """
        Метод возвращает пользователей с самой большой разностиью
        очков достижений
        Args:
            -
        Returns:
            list[tuple[Users, Users, int]] - список с парами пользователей
            и разностью их очков
        """
        users_with_max_score = self.get_users_with_max_score()
        users_with_min_score = self.get_users_with_min_score()
        result = []
        for top_user, top_score in users_with_max_score:
            for low_user, low_score in users_with_min_score:
                result.append((top_user, low_user, abs(top_score-low_score)))

        return result

    def get_users_with_min_gap(
        self
    ) -> list[tuple[Users, Users, int]]:
        """
        Метод возвращает пользователей с самой меленькой разностиью
        очков достижений
        Args:
            -
        Returns:
            list[tuple[Users, Users, int]] - список с парами пользователей
            и разностью их очков
        """
        score_column = func.sum(
            case(
                (Achievements.achievement_value is None, 0),
                else_=Achievements.achievement_value
            )
        ).label('Score')
        users_scores = select(
            Users,
            score_column
        ).join(
            UsersAchievements,
            UsersAchievements.c.get('user_id') == Users.id,
            isouter=True
        ).join(
            Achievements,
            UsersAchievements.c.get('achievement_id') == Achievements.id,
            isouter=True
        ).group_by(
            Users.id
        ).order_by(
            'Score'
        )

        users_scores_sequence = self.session.execute(users_scores).all()

        min_gap = users_scores_sequence[-1][1]
        result: list[tuple[Users, Users, int]] = []

        for i, (user, score) in enumerate(users_scores_sequence[:-1]):
            next_user = users_scores_sequence[i+1][0]
            next_score = users_scores_sequence[i+1][1]
            gap = abs(score - next_score)
            if gap < min_gap:
                min_gap = gap
                result.clear()
                result.append((user, next_user, gap))
            elif gap == min_gap:
                result.append((user, next_user, gap))

        return result

    def get_users_with_7_days_streak(
        self
    ) -> list[Users]:
        """
        Метод возвращает список пользоватлей, которые
        когда-либо получали достижения 7 дней подряд
        Args:
            -
        Returns:
            list[Users] - списко объектов пользователей
        """
        get_achievements_with_dates = select(
            UsersAchievements.c.get('user_id'),
            UsersAchievements.c.get('date')
        ).order_by(
            UsersAchievements.c.get('user_id'),
            UsersAchievements.c.get('date')
        )

        achievements_with_dates = self.session.execute(
            get_achievements_with_dates
        ).all()

        users_dates_dict: dict[int, list[date]] = {}
        current_user_id = achievements_with_dates[0][0]
        users_dates_dict[current_user_id] = []

        for user_id, achievement_date in achievements_with_dates:
            if user_id == current_user_id:
                users_dates_dict[current_user_id].append(achievement_date)
            else:
                users_dates_dict[user_id] = []
                users_dates_dict[user_id].append(achievement_date)
                current_user_id = user_id

        users_with_streak = []
        for user_id, user_dates in users_dates_dict.items():

            streak = 1
            for i, achievement_date in enumerate(user_dates[:-1]):

                next_date = user_dates[i+1]

                if next_date - achievement_date == timedelta(1):
                    streak += 1
                elif next_date - achievement_date > timedelta(1):
                    streak = 1

                if streak == 7:
                    users_with_streak.append(user_id)
                    break

        get_users_with_streak = select(
            Users
        ).where(
            Users.id.in_(users_with_streak)
        )

        sqlalchemy_result = self.session.execute(
            get_users_with_streak
        ).all()

        result = [row[0] for row in sqlalchemy_result]

        return result
