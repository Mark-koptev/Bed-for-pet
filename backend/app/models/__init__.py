from database.database import Base


def init_models(engine):    # Здесь вы можете добавить все ваши модели
    __all__ = ["User"]
    Base.metadata.create_all(bind=engine)
