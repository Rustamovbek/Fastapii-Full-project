from sqladmin import ModelView
from models.lesson import Lesson

class LessonAdmin(ModelView, model=Lesson):
    column_list = [Lesson.id, Lesson.course_id, Lesson.title, Lesson.author_id]
    column_searchable_list = [Lesson.title]
    column_sortable_list = [Lesson.id]