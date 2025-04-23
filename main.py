from fastapi import FastAPI
from routers.lesson import router as lesson_router
from routers.course import router as course_router
from routers.rating import router as rating_router
from routers.comment import router as comment_router
from routers.auth import router as auth_router
from core.database import engine
from models import user
app = FastAPI()

user.Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(course_router)
app.include_router(lesson_router)
app.include_router(comment_router)
app.include_router(rating_router)