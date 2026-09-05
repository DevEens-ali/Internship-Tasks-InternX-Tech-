from fastapi import FastAPI
from app.database import engine, Base
from app import models

from app.routers import auth, users
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    description="REST API with JWT Authentication and CRUD Operations",
    version="1.0.0"
)

app.include_router(auth.router)

app.include_router(users.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}