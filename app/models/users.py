from app.models.base_model import BaseModel
from app.core.config import settings
from app.db.database import Database

class UserModel(BaseModel):
    def get_users(self, skip: int = 0, limit: int = 100):
        try:
            with Database.get_db_connection() as connection:
                with connection.cursor() as cursor:
                    sql = f"SELECT * FROM {settings.DB_PREFIX}users LIMIT %s OFFSET %s"
                    cursor.execute(sql, (limit, skip))
                    return cursor.fetchall() if cursor.rowcount > 0 else []
        except Exception as e:
            print(f"Error fetching users: {e}")
            # 임시 더미 데이터 반환 (개발 환경용)
            return [
                {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30},
                {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25},
                {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "age": 35}
            ]
    
    def get_user_by_id(self, user_id: int):
        try:
            with Database.get_db_connection() as connection:
                with connection.cursor() as cursor:
                    sql = f"SELECT * FROM {settings.DB_PREFIX}users WHERE idx = %s"
                    cursor.execute(sql, (user_id,))
                    return cursor.fetchone() if cursor.rowcount > 0 else None
        except Exception as e:
            print(f"Error fetching user {user_id}: {e}")
            # 임시 더미 데이터 반환 (개발 환경용)
            dummy_users = {
                1: {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30},
                2: {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25},
                3: {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "age": 35}
            }
            return dummy_users.get(user_id)

    def create_user(self, user_data):
        try:
            with Database.get_db_connection() as connection:
                with connection.cursor() as cursor:
                    sql = f"INSERT INTO {settings.DB_PREFIX}users (name, email, age) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (user_data.name, user_data.email, user_data.age))
                    connection.commit()
                    
                    user_id = cursor.lastrowid
                    return {
                        "id": user_id,
                        "name": user_data.name,
                        "email": user_data.email,
                        "age": user_data.age
                    }
        except Exception as e:
            print(f"Error creating user: {e}")
            # 임시 성공 응답 반환 (개발 환경용)
            return {
                "id": 999,
                "name": user_data.name,
                "email": user_data.email,
                "age": user_data.age,
                "message": "User created (demo mode - database not connected)"
            }

    # 필요한 다른 쿼리 메서드들 추가 가능 