from pydantic import BaseModel, ConfigDict
from schemas.user import UserOut

class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class CourseOut(BaseModel):
    id: int
    title: str
    description: str
    author: UserOut

    model_config = ConfigDict(from_attributes=True)