import pymysql
from app.core.config import settings
from contextlib import contextmanager

class Database:
    @staticmethod
    def get_connection():
        try:
            return pymysql.connect(
                host=settings.DB_HOST,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                db=settings.DB_DATABASE,
                port=int(settings.DB_PORT),
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            print(f"Database connection failed: {e}")
            return None
    
    @staticmethod
    @contextmanager
    def get_db_connection():
        """데이터베이스 연결을 컨텍스트 매니저로 관리"""
        connection = None
        try:
            connection = Database.get_connection()
            if connection is None:
                raise Exception("Database connection failed")
            yield connection
        except Exception as e:
            print(f"Database operation failed: {e}")
            raise
        finally:
            if connection:
                connection.close() 