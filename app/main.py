from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="테스트 개발용 API 문서입니다.",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI 경로
    redoc_url="/redoc",  # ReDoc 경로
    contact={
        "name": "신현승",
        "email": "dev@example.com",
    },
    license_info={
        "name": "Private",
    }
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI project"}