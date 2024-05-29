from sqladmin import Admin, ModelView
from database.database import engine
from models.user import User1


class UserAdmin(ModelView, model=User1):
    column_list = "__all__"


def init_admin_app(app):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
