from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud.rating as crud_comment
from core.auth import get_db
from core.auth import get_current_user
from schemas.rating import RatingResponse, AverageRatingResponse, RatingCreate

router = APIRouter(prefix="/rating", tags=["Rating-API"])

@router.post("/rate", response_model=RatingResponse)
def rate_lesson(
    rating: RatingCreate,
    db: Session = Depends(get_db),
    user: dict = Depends(get_current_user)
):
    return crud_comment.add_or_update_rating(db, user["id"], rating)

@router.get("/lesson/{lesson_id}/average-rating", response_model=AverageRatingResponse)
def get_average_lesson_rating(
    lesson_id: int,
    db: Session = Depends(get_db)
):
    average = crud_comment.get_average_rating(db, lesson_id)
    return {"lesson_id": lesson_id, "average_rating": average}
