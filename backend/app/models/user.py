from sqlalchemy import Column, Integer, String
from database.database import Base, storage
from fastapi_storages.integrations.sqlalchemy import FileType


class User1(Base):
    __tablename__ = "users1"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    avatar = Column(FileType(storage=storage), nullable=True)
