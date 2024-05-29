from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import FILE_PATH, settings
from fastapi_storages import FileSystemStorage
DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
storage = FileSystemStorage(path=FILE_PATH)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
