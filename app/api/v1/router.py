from fastapi import APIRouter
from app.api.v1.endpoints import users  # 여기에 새로운 엔드포인트 모듈을 import

api_router = APIRouter()

# 여기에 라우터들을 include_router로 추가
api_router.include_router(users.router, tags=["users"])

# 새로운 라우터를 추가할 때는 여기에 한 줄만 추가하면 됩니다
# 예: api_router.include_router(posts.router, tags=["posts"]) 