from fastapi import FastAPI

from models import init_models
from database.database import engine
from models.user import User
from api.v1 import user as user_api
app = FastAPI()

init_models()

app.include_router(user_api.router, prefix="/api/v1/users", tags=["users"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
