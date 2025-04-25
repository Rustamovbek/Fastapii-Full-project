from sqladmin import ModelView
from models.comment import Comment

class CommentAdmin(ModelView, model=Comment):
    column_list = [Comment.id, Comment.lesson_id, Comment.user_id]
    column_searchable_list = [Comment.lesson_id]
    column_sortable_list = [Comment.user_id]
