from sqlalchemy.orm import relationship

from core.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    courses = relationship("Course", back_populates="author")
    lessons = relationship("Lesson", back_populates="author")

    def __str__(self):
        return f"{self.id, self.full_name, self.email, self.is_admin}"