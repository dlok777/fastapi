# FAST API

FastAPI를 사용한 고성능 REST API 서버입니다.

## 🚀 Features

- RESTful API
- MySQL 데이터베이스 연동
- 자동 API 문서화 (Swagger/ReDoc)
- 환경 변수 기반 설정

## 🛠 Tech Stack

- Python 3.8+
- FastAPI
- PyMySQL
- uvicorn

## 🏃‍♂️ FASTAPI 및 필수 패키지 설치
pip install fastapi uvicorn

## 🏃‍♂️ 기본 실행
uvicorn app.main:app --reload

# 🏃‍♂️ 호스트와 포트 지정하여 실행
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload