# FastAPI Project - 고성능 REST API 서버

FastAPI를 기반으로 한 확장 가능하고 유지보수하기 쉬운 REST API 서버입니다. 계층화된 아키텍처와 의존성 주입을 활용하여 Clean Architecture 원칙을 따르는 프로젝트입니다.

## 🏃‍♂️ FASTAPI 및 필수 패키지 설치
pip install fastapi uvicorn

## 🏃‍♂️ 기본 실행
uvicorn app.main:app --reload

## 🏃‍♂️ 호스트와 포트 지정하여 실행
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

## �� 목차

- [프로젝트 개요](#-프로젝트-개요)
- [아키텍처 구조](#-아키텍처-구조)
- [기술 스택](#-기술-스택)
- [설치 및 실행](#-설치-및-실행)
- [API 문서](#-api-문서)
- [주요 기능](#-주요-기능)
- [개발 가이드](#-개발-가이드)
- [아키텍처 분석](#-아키텍처-분석)

## 🎯 프로젝트 개요

### **개발 목적**
- FastAPI 모범 사례를 적용한 확장 가능한 API 서버 구축
- 계층화된 아키텍처를 통한 유지보수성 향상
- 의존성 주입을 활용한 테스트 용이성 확보
- 실무에서 바로 사용할 수 있는 프로덕션 레벨 코드 작성

### **주요 특징**
- ✅ **Clean Architecture**: 관심사 분리와 의존성 방향 제어
- ✅ **의존성 주입**: FastAPI Depends를 활용한 느슨한 결합
- ✅ **서비스 계층**: 비즈니스 로직과 데이터 액세스 분리
- ✅ **예외 처리**: 계층별 적절한 오류 처리
- ✅ **개발 친화적**: 데이터베이스 없이도 API 테스트 가능

## ��️ 아키텍처 구조

### **전체 디렉토리 구조**

├── app/ # 메인 애플리케이션 패키지
│ ├── main.py # 애플리케이션 진입점
│ ├── api/ # API 계층
│ │ └── v1/ # API 버전 관리
│ │ ├── router.py # 라우터 통합 관리
│ │ └── endpoints/ # 엔드포인트 정의
│ │ └── users.py # 사용자 관련 API
│ ├── services/ # 서비스 계층 (비즈니스 로직)
│ │ ├── init.py # 패키지 선언
│ │ └── users.py # 사용자 서비스
│ ├── models/ # 모델 계층 (데이터 액세스)
│ │ ├── base_model.py # 기본 모델 클래스
│ │ └── users.py # 사용자 모델
│ ├── db/ # 데이터베이스 계층
│ │ └── database.py # 데이터베이스 연결 관리
│ └── core/ # 핵심 설정 및 유틸리티
│ ├── config.py # 환경 설정 관리
│ └── security.py # 보안 관련 기능
├── README.md # 프로젝트 문서
└── .gitignore # Git 무시 파일


### **계층별 역할**

#### **1. API 계층 (`app/api/`)**
- **역할**: HTTP 요청/응답 처리
- **주요 파일**: `endpoints/users.py`
- **기능**: 
  - 엔드포인트 정의 및 라우팅
  - 요청 데이터 검증 (Pydantic 모델)
  - HTTP 상태 코드 및 응답 형식 관리
  - 의존성 주입을 통한 서비스 계층 호출

#### **2. 서비스 계층 (`app/services/`)**
- **역할**: 비즈니스 로직 처리
- **주요 파일**: `users.py`
- **기능**:
  - 비즈니스 규칙 검증
  - 데이터 정규화 및 포맷팅
  - 모델 계층 호출 및 결과 처리
  - 예외 처리 및 오류 메시지 생성

#### **3. 모델 계층 (`app/models/`)**
- **역할**: 데이터 액세스 로직
- **주요 파일**: `users.py`, `base_model.py`
- **기능**:
  - 데이터베이스 쿼리 실행
  - SQL 문 작성 및 파라미터 바인딩
  - 데이터베이스 연결 관리
  - 개발 환경용 더미 데이터 제공

#### **4. 데이터베이스 계층 (`app/db/`)**
- **역할**: 데이터베이스 연결 관리
- **주요 파일**: `database.py`
- **기능**:
  - MySQL 연결 설정
  - 컨텍스트 매니저를 통한 안전한 연결 관리
  - 연결 실패 시 예외 처리

#### **5. 핵심 설정 (`app/core/`)**
- **역할**: 애플리케이션 설정 및 유틸리티
- **주요 파일**: `config.py`, `security.py`
- **기능**:
  - 환경 변수 기반 설정 관리
  - 데이터베이스 연결 정보
  - 보안 관련 설정

## ��️ 기술 스택

### **Backend Framework**
- **FastAPI 0.116.1**: 고성능 웹 프레임워크
- **Python 3.10+**: 최신 Python 기능 활용

### **데이터베이스**
- **PyMySQL**: MySQL 데이터베이스 연결
- **MySQL**: 관계형 데이터베이스

### **데이터 검증 및 설정**
- **Pydantic**: 데이터 검증 및 직렬화
- **Pydantic Settings**: 환경 변수 기반 설정 관리

### **서버**
- **Uvicorn**: ASGI 서버

### **아키텍처 패턴**
- **Clean Architecture**: 관심사 분리
- **Dependency Injection**: 의존성 주입
- **Layered Architecture**: 계층화된 구조
- **Repository Pattern**: 데이터 액세스 추상화

## 🚀 설치 및 실행

### **1. 저장소 클론**
```bash
git clone <repository-url>
cd fastapi
```

### **2. Python 환경 확인**
```bash
python --version  # Python 3.10+ 필요
```

### **3. 의존성 설치**
```bash
pip install fastapi uvicorn pymysql pydantic-settings
```

### **4. 환경 변수 설정 (선택사항)**
```bash
# .env 파일 생성 (프로젝트 루트에)
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_DATABASE=fastapi_db
DB_PREFIX=
```

### **5. 서버 실행**

#### **개발 모드 (권장)**
```bash
uvicorn app.main:app --reload
```

#### **프로덕션 모드**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

#### **특정 포트 지정**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## �� API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

## 🎯 주요 기능

### **사용자 관리 API**

#### **1. 사용자 목록 조회**
```http
GET /api/v1/users/
```

**쿼리 파라미터:**
- `skip` (int, 선택): 건너뛸 레코드 수 (기본값: 0)
- `limit` (int, 선택): 가져올 최대 레코드 수 (기본값: 100)

**응답 예시:**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "age": 25
  }
]
```

#### **2. 특정 사용자 조회**
```http
GET /api/v1/users/{user_id}
```

**경로 파라미터:**
- `user_id` (int, 필수): 조회할 사용자의 ID

**응답 예시:**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
```

#### **3. 새 사용자 생성**
```http
POST /api/v1/users/
```

**요청 본문:**
```json
{
  "name": "New User",
  "email": "newuser@example.com",
  "age": 28
}
```

**응답 예시:**
```json
{
  "id": 4,
  "name": "New User",
  "email": "newuser@example.com",
  "age": 28
}
```

#### **4. 사용자 통계 조회**
```http
GET /api/v1/users/statistics/
```

**응답 예시:**
```json
{
  "total_users": 3,
  "active_users": 2,
  "age_distribution": {
    "18-25": 1,
    "26-35": 2,
    "36-50": 0,
    "50+": 0,
    "unknown": 0
  },
  "average_age": 27.5,
  "email_domains": {
    "example.com": 3
  }
}
```

### **데이터 검증 기능**

#### **사용자 생성 시 검증 규칙**
- **이름**: 필수 입력, 공백 제거
- **이메일**: 필수 입력, 이메일 형식 검증 (`@` 포함)
- **나이**: 선택 입력, 0-150 범위 검증

#### **페이지네이션**
- **skip**: 음수 값 자동 0으로 정규화
- **limit**: 0 이하 시 100으로, 1000 초과 시 1000으로 제한

## 🔧 개발 가이드

### **새로운 API 엔드포인트 추가**

#### **1. 엔드포인트 생성**
```python
# app/api/v1/endpoints/posts.py
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.posts import PostService

router = APIRouter()

class Post(BaseModel):
    title: str
    content: str
    author_id: int

def get_post_service():
    return PostService()

@router.get("/posts/")
def read_posts(post_service: PostService = Depends(get_post_service)):
    return post_service.get_posts()
```

#### **2. 서비스 로직 추가**
```python
# app/services/posts.py
from app.models.posts import PostModel
from typing import List, Dict, Any

class PostService:
    def __init__(self):
        self.post_model = PostModel()
    
    def get_posts(self) -> List[Dict[str, Any]]:
        return self.post_model.get_posts()
```

#### **3. 모델 로직 추가**
```python
# app/models/posts.py
from app.models.base_model import BaseModel
from app.db.database import Database

class PostModel(BaseModel):
    def get_posts(self):
        try:
            with Database.get_db_connection() as connection:
                with connection.cursor() as cursor:
                    sql = "SELECT * FROM posts"
                    cursor.execute(sql)
                    return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching posts: {e}")
            return []
```

#### **4. 라우터 등록**
```python
# app/api/v1/router.py
from app.api.v1.endpoints import users, posts

api_router = APIRouter()
api_router.include_router(users.router, tags=["users"])
api_router.include_router(posts.router, tags=["posts"])  # 새로 추가
```

### **의존성 주입 활용**

#### **서비스 계층 주입**
```python
def get_user_service():
    return UserService()

@router.get("/users/")
def read_users(user_service: UserService = Depends(get_user_service)):
    return user_service.get_users()
```

#### **데이터베이스 연결 주입**
```python
def get_db():
    db = Database.get_connection()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/")
def read_users(db = Depends(get_db)):
    # db 객체를 사용하여 데이터베이스 작업
    pass
```

## �� 아키텍처 분석

### **데이터 흐름**
클라이언트 요청
↓
FastAPI 라우터 (app/main.py)
↓
API 엔드포인트 (app/api/v1/endpoints/users.py)
↓
서비스 계층 (app/services/users.py) - 비즈니스 로직
↓
모델 계층 (app/models/users.py) - 데이터 액세스
↓
데이터베이스 계층 (app/db/database.py) - 연결 관리
↓
MySQL 데이터베이스 (또는 더미 데이터)
↓
응답 반환

### **아키텍처 점수**

| 항목 | 점수 | 설명 |
|------|------|------|
| **확장성** | ⭐⭐⭐⭐⭐ | 새로운 기능 추가 용이 |
| **유지보수성** | ⭐⭐⭐⭐⭐ | 코드 구조가 명확함 |
| **테스트 용이성** | ⭐⭐⭐⭐ | 의존성 주입으로 테스트 가능 |
| **성능** | ⭐⭐⭐⭐ | 효율적인 데이터베이스 연결 관리 |
| **안정성** | ⭐⭐⭐⭐ | 예외 처리와 오류 관리 |
| **가독성** | ⭐⭐⭐⭐⭐ | 명확한 파일 구조와 네이밍 |

**총점: 28/30 (93%)** ��

### **장점**

1. **Clean Architecture 원칙 준수**
   - 의존성 방향이 올바름 (외부 → 내부)
   - 각 계층의 책임이 명확함
   - 비즈니스 로직이 외부 의존성과 분리됨

2. **FastAPI 모범 사례 적용**
   - `Depends`를 사용한 의존성 주입
   - Pydantic 모델을 활용한 데이터 검증
   - 자동 API 문서화

3. **확장 가능한 구조**
   - 새로운 API 엔드포인트 추가 용이
   - 서비스 계층에서 비즈니스 로직 재사용
   - 모델 계층에서 데이터 액세스 로직 분리

4. **개발자 경험 (DX) 향상**
   - 명확한 파일 구조
   - 자동 코드 리로드
   - 직관적인 네이밍

### **개선 가능한 부분**

1. **로깅 시스템**
   - 현재는 print문 사용
   - 구조화된 로깅 필요

2. **캐싱 레이어**
   - 자주 조회되는 데이터 캐싱
   - Redis 등 외부 캐시 도입

3. **단위 테스트**
   - 각 계층별 테스트 코드
   - Mock을 활용한 격리 테스트

4. **환경별 설정**
   - 개발/스테이징/프로덕션 환경 분리
   - 환경별 데이터베이스 설정

## �� 테스트

### **API 테스트 예시**

#### **사용자 목록 조회**
```bash
curl http://localhost:8000/api/v1/users/
```

#### **특정 사용자 조회**
```bash
curl http://localhost:8000/api/v1/users/1
```

#### **새 사용자 생성**
```bash
curl -X POST http://localhost:8000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Smith", "email": "jane@example.com", "age": 25}'
```

#### **사용자 통계 조회**
```bash
curl http://localhost:8000/api/v1/users/statistics/
```

### **브라우저 테스트**
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## �� 디버깅

### **개발 환경 디버깅**
프로젝트는 개발 환경에서 데이터베이스 연결 실패 시 자동으로 더미 데이터를 제공합니다:

```python
# 데이터베이스 연결 실패 시 더미 데이터 반환
return [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "age": 35}
]
```

### **로그 확인**
서버 실행 시 다음과 같은 로그를 확인할 수 있습니다: