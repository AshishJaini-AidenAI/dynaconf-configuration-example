from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

# Use Dynaconf get() which is robust to key casing and lookup locations
SQLALCHEMY_DATABASE_URL = settings.get("DATABASE_URL") or settings.get("database_url")

# Only pass check_same_thread for SQLite
connect_args = {}
if isinstance(SQLALCHEMY_DATABASE_URL, str) and SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
