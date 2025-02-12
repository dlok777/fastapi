from typing import Generator
from fastapi import Depends, HTTPException, status

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close() 