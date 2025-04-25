from sqladmin import ModelView
from models.user import User

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.full_name, User.email, User.is_admin, User.courses, User.lessons]
    column_searchable_list = [User.email]
    column_sortable_list = [User.id]