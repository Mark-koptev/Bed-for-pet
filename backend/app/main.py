from fastapi import FastAPI
from models import init_models
from database.database import engine
from api.v1 import user as user_api
from admin.admin_panel import init_admin_app
app = FastAPI()

init_models(engine)
init_admin_app(app)
app.include_router(user_api.router, prefix="/api/v1/users", tags=["users"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="localhost", port=8000, reload=True)
