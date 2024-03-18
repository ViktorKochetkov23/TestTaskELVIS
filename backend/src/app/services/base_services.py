"""
Модуль с базовыми классами для сервисов приложения
"""
from fastapi import Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import UpdateBase
from sqlalchemy.exc import DBAPIError

from app.database import get_session


class BaseService:
    """
    Базовый класс для сервисов, работающих с базой данных
    """
    def __init__(
        self,
        session: Session = Depends(get_session)
    ):
        """
        Конструктор
        Args:
            session: Session - объект сессии
        Returns:
            None
        """
        self.session = session


class UpdateBaseService(BaseService):
    """
    Базовый класс для классов, имеющих возможность
    менять содержимое базы данных
    """
    def execute_update_statement(
        self,
        statement: UpdateBase
    ) -> dict:
        """
        Метод для выполнения выражения, которое меняет содержимое базы данных
        Args:
            statement: UpdateBase - выражение
        Returns:
            dict со статусом изменения
        """
        result = {}

        try:
            self.session.execute(statement)
            self.session.commit()
            result['Status'] = 'Success'
            result['Message'] = 'None'
        except DBAPIError as exc:
            self.session.rollback()
            self.session.flush()
            result['Status'] = 'Fail'
            result['Message'] = repr(exc)

        return result
