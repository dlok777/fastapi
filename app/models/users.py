from app.models.base_model import BaseModel
from app.core.config import settings

class UserModel(BaseModel):
    def __init__(self):
        super().__init__()

    def get_users(self, skip: int = 0, limit: int = 100):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM {settings.DB_PREFIX}users LIMIT %s OFFSET %s"
                
                cursor.execute(sql, (limit, skip))

                # last query 찍어보기
                # return cursor._executed;

                return cursor.fetchall() if cursor.rowcount > 0 else []
        finally:
            self.connection.close()
    
    def get_user_by_id(self, user_id: int):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM {settings.DB_PREFIX}users WHERE idx = %s"
                cursor.execute(sql, (user_id,))

                
                return cursor.fetchone() if cursor.rowcount > 0 else None
        finally:
            self.connection.close()

    def create_user(self, user_data):
        try:
            with self.connection.cursor() as cursor:
                sql = f"INSERT INTO {settings.DB_PREFIX}users (name, email, age) VALUES (%s, %s, %s)"
                cursor.execute(sql, (user_data.name, user_data.email, user_data.age))
                self.connection.commit()
                
                # 생성된 사용자의 ID 가져오기
                user_id = cursor.lastrowid
                
                # 생성된 사용자 정보 반환
                return {
                    "id": user_id,
                    "name": user_data.name,
                    "email": user_data.email,
                    "age": user_data.age
                }
        finally:
            self.connection.close()

    # 필요한 다른 쿼리 메서드들 추가 가능 