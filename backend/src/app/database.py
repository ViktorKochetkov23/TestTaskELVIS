"""
Файл настроек базы данных
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import settings


engine = create_engine(settings.get_database_url())


Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    """Функция получения новой сессии"""
    session = Session()
    try:
        yield session
    finally:
        session.close()
