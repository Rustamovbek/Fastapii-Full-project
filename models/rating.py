from sqlalchemy import Column, Integer, ForeignKey
from core.database import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    stars = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.id, self.user_id, self.lesson_id, self.stars}"