from app.models.users import UserModel
from typing import List, Optional, Dict, Any

class UserService:
    def __init__(self):
        self.user_model = UserModel()
    
    def get_users(self, skip: int = 0, limit: int = 100) -> List[Dict[str, Any]]:
        """사용자 목록을 조회합니다."""
        if skip < 0:
            skip = 0
        if limit <= 0 or limit > 1000:
            limit = 100
            
        return self.user_model.get_users(skip=skip, limit=limit)
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """ID로 사용자를 조회합니다."""
        if user_id <= 0:
            return None
            
        return self.user_model.get_user_by_id(user_id)
    
    def create_user(self, user_data) -> Dict[str, Any]:
        """새로운 사용자를 생성합니다."""
        # 비즈니스 로직 검증
        if not user_data.name or len(user_data.name.strip()) == 0:
            raise ValueError("Name is required")
        
        if not user_data.email or len(user_data.email.strip()) == 0:
            raise ValueError("Email is required")
        
        # 이메일 형식 검증 (간단한 검증)
        if '@' not in user_data.email:
            raise ValueError("Invalid email format")
        
        # 나이 검증
        if user_data.age is not None and (user_data.age < 0 or user_data.age > 150):
            raise ValueError("Age must be between 0 and 150")
        
        return self.user_model.create_user(user_data) 