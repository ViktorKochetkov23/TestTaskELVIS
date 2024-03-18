from typing import List, Any

from fastapi import Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import  UpdateBase

from app.database import get_session


class BaseService:


    def __init__(self,
        session: Session = Depends(get_session)
    ):
        """
        Конструктор

        Принимает объект сессии session класса Session

        Возвращает None
        """
        self.session = session


class UpdateBaseService(BaseService):


    def execute_update_statement(
        self,
        statement: UpdateBase
    ) -> dict:
        
        result = {}

        try:
            self.session.execute(statement)
            self.session.commit()
            result['Status'] = 'Success'
            result['Message'] = 'None'
        except Exception as e:
            self.session.rollback()
            self.session.flush()
            result['Status'] = 'Fail'
            result['Message'] = repr(e)
        
        return result
