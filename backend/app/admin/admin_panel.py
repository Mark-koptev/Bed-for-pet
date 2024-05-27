# app/admin.py
from fastapi_admin.app import app as admin_app
from fastapi_admin.widgets import inputs
from fastapi_admin.models import AbstractAdmin

from models.user import User

admin_app.configure(
    templates_dir="./app/templates",
    database_url="sqlite+aiosqlite:///./test.db",
)


class UserAdmin(AbstractAdmin):
    model = User
    search_fields = [User.username]
    fields = [
        inputs.Input('username'),
        inputs.Input('email'),
        inputs.Input('full_name'),
        inputs.Input('hashed_password'),
    ]


admin_app.register(UserAdmin)
