"""
Определения класса настроек
"""
from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Этот класс предоставляет настройки приложения
    """

    server_host: str
    """IP-адрес хоста"""
    server_port: int
    """Порт приложения"""


    class Config:
        """Настройки окружения программы."""

        env_file = '.env'
        """Имя файла с переменными окружения"""
        env_file_encoding = 'utf-8'
        """кодировка env_file"""


settings = Settings(
    _env_file=Path(__file__).parents[1].resolve()/".env",
    _env_file_encoding='utf-8'
)
