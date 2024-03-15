"""
Запуск приложения
"""
import uvicorn
from app.settings import settings


uvicorn.run(
    "app.app:app",
    host=settings.server_host,
    port=settings.server_port,
    reload=True
)
