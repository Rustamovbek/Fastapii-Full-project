from fastapi import FastAPI
from routers.lesson import router as lesson_router
from routers.course import router as course_router
from routers.rating import router as rating_router
from routers.comment import router as comment_router
from routers.auth import router as auth_router
from core.database import engine
from models import user
from sqladmin import Admin
from admin.user import UserAdmin
from admin.course import CourseAdmin
from admin.lesson import LessonAdmin
from admin.comment import CommentAdmin
from admin.rating import RatingAdmin
app = FastAPI()

user.Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(course_router)
app.include_router(lesson_router)
app.include_router(comment_router)
app.include_router(rating_router)

admin = Admin(app, engine)
admin.add_view(UserAdmin)
admin.add_view(CourseAdmin)
admin.add_view(LessonAdmin)
admin.add_view(CommentAdmin)
admin.add_view(RatingAdmin)