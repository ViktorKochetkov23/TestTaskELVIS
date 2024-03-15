"""
Файл настроек базы данных
"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from backend.src.app.settings import settings


engine = create_engine(settings.database_url)
Base = declarative_base()
metadata = MetaData()

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
