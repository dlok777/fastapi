import pymysql
from app.core.config import settings

class Database:
    @staticmethod
    def get_connection():
        return pymysql.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            db=settings.DB_DATABASE,
            port=int(settings.DB_PORT),
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        ) 