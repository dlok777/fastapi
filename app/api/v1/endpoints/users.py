from typing import List
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.users import UserService

router = APIRouter()

# Pydantic 모델 정의
class User(BaseModel):
    name: str
    email: str
    age: int = None

# 의존성 주입
def get_user_service():
    return UserService()

"""
사용자 목록을 조회합니다.
- **skip**: 건너뛸 레코드 수
- **limit**: 가져올 최대 레코드 수
"""
@router.get("/users/")
def read_users(
    skip: int = 0, 
    limit: int = 100,
    user_service: UserService = Depends(get_user_service)
): 
    try:
        users = user_service.get_users(skip=skip, limit=limit)
        if not users:
            raise HTTPException(status_code=404, detail="Users not found")
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

"""
특정 사용자를 조회합니다.
- **user_id**: 조회할 사용자의 ID
"""
@router.get("/users/{user_id}")
def read_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    try:
        user = user_service.get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

"""
새로운 사용자를 생성합니다.
"""
@router.post("/users/")
def create_user(
    user: User,
    user_service: UserService = Depends(get_user_service)
):
    try:
        result = user_service.create_user(user)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

"""
사용자 통계 정보를 조회합니다.
"""
@router.get("/users/statistics/")
def get_user_statistics(
    user_service: UserService = Depends(get_user_service)
):
    try:
        statistics = user_service.get_user_statistics()
        return statistics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


