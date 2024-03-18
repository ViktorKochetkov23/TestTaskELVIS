"""
Определения класса настроек
"""
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Этот класс предоставляет настройки приложения
    """

    server_host: str
    """IP-адрес хоста"""
    server_port: int
    """Порт приложения"""
    database_name: str
    """Имя базы данных"""
    database_user: str
    """Имя пользователя базы данных"""
    database_host: str
    """IP-адрес сервера базы данных"""
    database_port: int
    """Порт базы данных"""
    database_password: str
    """Пароль пользователя базы данных"""

    def get_database_url(
        self
    ) -> str:
        """Метод возвращает строку подключения к базе данных"""

        return f'postgresql+psycopg2://{self.database_user}:' + \
            f'{self.database_password}@' + \
            f'{self.database_host}:' + \
            f'{self.database_port}/' + \
            f'{self.database_name}'

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
