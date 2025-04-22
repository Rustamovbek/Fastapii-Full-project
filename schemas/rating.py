from pydantic import BaseModel, Field, ConfigDict

class RatingCreate(BaseModel):
    lesson_id: int
    stars: int = Field(..., ge=1, le=5)

class RatingResponse(BaseModel):
    id: int
    user_id: int
    lesson_id: int
    stars: int

    model_config = ConfigDict(from_attributes=True)

class AverageRatingResponse(BaseModel):
    lesson_id: int
    average_rating: float