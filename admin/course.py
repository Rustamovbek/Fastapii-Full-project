from sqladmin import ModelView
from models.course import Course

class CourseAdmin(ModelView, model=Course):
    column_list = [Course.id, Course.title, Course.description, Course.author]
    column_searchable_list = [Course.title]
    column_sortable_list = [Course.id]
