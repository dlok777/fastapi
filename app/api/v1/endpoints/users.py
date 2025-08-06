from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.users import UserModel

router = APIRouter()

# Pydantic 모델 정의
class User(BaseModel):
    name: str
    email: str
    age: int = None


"""
사용자 목록을 조회합니다.
- **skip**: 건너뛸 레코드 수
- **limit**: 가져올 최대 레코드 수
"""
@router.get("/users/")
def read_users(skip: int = 0,limit: int = 100): 
    user_model = UserModel()

    users = user_model.get_users(skip=skip, limit=limit)

    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users



"""
사용자 목록을 조회합니다.
- **user_id**: 조회할 사용자의 ID
"""
@router.get("/users/{user_id}")
def read_user(user_id: int):
    
    user_model = UserModel()
    user = user_model.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users/")
def create_user(user: User):
    user_model = UserModel()
    result = user_model.create_user(user)
    return result


