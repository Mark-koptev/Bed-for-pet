from database.database import Base
from models.user import User


# Здесь вы можете добавить все ваши модели
__all__ = ["User", "Order"]


def init_models():
    from database.database import engine
    Base.metadata.create_all(bind=engine)
