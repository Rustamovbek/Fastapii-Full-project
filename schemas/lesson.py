from pydantic import BaseModel, HttpUrl
from typing import Optional

class LessonBase(BaseModel):
    course_id: int
    title: str
    video_url: Optional[HttpUrl] = None
    content: Optional[str] = None

class LessonCreate(LessonBase):
    pass

class LessonUpdate(BaseModel):
    title: Optional[str] = None
    video_url: Optional[HttpUrl] = None
    content: Optional[str] = None

class LessonOut(LessonBase):
    id: int

    class Config:
        from_attributes = True
