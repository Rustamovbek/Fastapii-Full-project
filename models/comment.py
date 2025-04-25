from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from core.database import Base

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __str__(self):
        return f"{self.id, self.user_id, self.lesson_id, self.text}"