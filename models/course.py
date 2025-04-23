from sqlalchemy.orm import relationship
from core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User")