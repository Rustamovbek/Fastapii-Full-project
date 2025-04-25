from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base

class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    title = Column(String(255), nullable=False)
    video_url = Column(String(500))
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="lessons")

    def __str__(self):
        return f"{self.id, self.course_id, self.title, self.author_id}"