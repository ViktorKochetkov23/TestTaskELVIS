"""
Описание таблиц базы данных
"""
from __future__ import annotations

from sqlalchemy import (Integer,
                        String,
                        Date,
                        Table,
                        Column,
                        ForeignKey)
from sqlalchemy.orm import (DeclarativeBase,
                            Mapped,
                            mapped_column,
                            relationship)


class Base(DeclarativeBase):
    """Базовый класс для таблиц БД"""
    pass


UsersAchievements = Table(
    "users_achievements",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("achievement_id", ForeignKey("achievements.id"), primary_key=True),
    Column("date", Date(), nullable=False)
)


class Users(Base):
    """Таблица 'users'"""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(30), nullable=False)
    language: Mapped[str] = mapped_column(nullable=False)
    achievements: Mapped[list[Achievements]] = relationship(
        secondary=UsersAchievements, back_populates="users"
    )


class Achievements(Base):
    """Таблица 'achievements'"""
    __tablename__ = "achievements"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    achievement_name: Mapped[str] = mapped_column(String(50), nullable=False)
    achievement_value: Mapped[int] = mapped_column(Integer, nullable=False)
    achievement_desc: Mapped[str] = mapped_column(String(150), nullable=False)
    users: Mapped[list[Users]] = relationship(
        secondary=UsersAchievements, back_populates="achievements"
    )
