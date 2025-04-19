from typing import Optional, Any, List
from pydantic import BaseModel
from sqlalchemy.orm import relationship

from database import Base
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

class BaseResponse(BaseModel):
    status: bool = True
    data: Optional[Any] = None
    errors: Optional[List[dict]] = None
