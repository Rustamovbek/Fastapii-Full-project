from sqladmin import ModelView
from models.rating import Rating

class RatingAdmin(ModelView, model=Rating):
    column_list = [Rating.id, Rating.lesson_id, Rating.user_id]
    column_searchable_list = [Rating.lesson_id]
    column_sortable_list = [Rating.user_id]