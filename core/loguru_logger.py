from loguru import logger
import sys
import os
from django.conf import settings

LOG_DIR = os.path.join(settings.BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logger.remove()

logger.add(sys.stdout, level="INFO", backtrace=True, diagnose=True, format="<green>{time}</green> | <level>{level}</level> | <cyan>{name}:{function}:{line}</cyan> - <level>{message}</level>")

logger.add(
    os.path.join(LOG_DIR, "app.log"),
    rotation="10 MB",
    retention="7 days",
    compression="zip",
    level="DEBUG",
    backtrace=True,
    diagnose=True,
    enqueue=True
)
