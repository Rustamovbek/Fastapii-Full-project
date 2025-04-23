from fastapi import APIRouter
import crud.rating as crud_comment
from schemas.rating import RatingResponse, AverageRatingResponse, RatingCreate
from core.dependencies import DBSessionDep, CurrentUserDep
router = APIRouter(prefix="/rating", tags=["Rating-API"])

@router.post("/rate", response_model=RatingResponse)
def rate_lesson(
    rating: RatingCreate,
    db: DBSessionDep,
    user: CurrentUserDep
):
    return crud_comment.add_or_update_rating(db, user["id"], rating)

@router.get("/lesson/{lesson_id}/average-rating", response_model=AverageRatingResponse)
def get_average_lesson_rating(
    lesson_id: int,
    db: DBSessionDep
):
    average = crud_comment.get_average_rating(db, lesson_id)
    return {"lesson_id": lesson_id, "average_rating": average}