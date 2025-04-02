from sqlalchemy.orm import Session
from database import get_db

from fastapi import APIRouter

app = APIRouter(
    prefix="/user",
    tags=["user"]
)

@app.get("/test")
async def user_test():
    return "test"