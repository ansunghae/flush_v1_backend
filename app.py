from fastapi import FastAPI

import models
from database import engine
models.Base.metadata.create_all(bind = engine)

app = FastAPI()

from router import user_router

app.include_router(user_router.app)

@app.get("/register")
async def root():
    return {"message": "Hello World"}