import os
from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent

# load_dotenv(BASE_DIR / ".env", override=True)

# DATABASE_URL = os.getenv("DATABASE_URL")

# if DATABASE_URL is None:
#     raise ValueError("DATABASE_URL not found in .env")

load_dotenv(BASE_DIR / ".env", override=True)

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE DRIVER:", DATABASE_URL.split("://")[0] if DATABASE_URL else None)

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not found in .env")

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {
            "ca": str(BASE_DIR / "aiven-ca.pem")
        }
    }
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()