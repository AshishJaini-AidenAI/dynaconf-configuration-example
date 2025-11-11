from fastapi import FastAPI
from . import models
from .database import engine
from .routes import router
from .config import settings

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.get("APP_NAME") or settings.get("app_name"), debug=settings.get("DEBUG") or settings.get("debug"))

app.include_router(router, prefix="/api", tags=["Books"])


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.app_name}"}
