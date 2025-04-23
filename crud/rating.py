from sqlalchemy.orm import Session
from models.rating import Rating
from schemas.rating import RatingCreate
from sqlalchemy import func

def add_or_update_rating(db: Session, user_id: int, rating: RatingCreate):
    db_rating = db.query(Rating).filter(
        Rating.user_id == user_id,
        Rating.lesson_id == rating.lesson_id
    ).first()

    if db_rating:
        db_rating.stars = rating.stars
    else:
        db_rating = Rating(user_id=user_id, lesson_id=rating.lesson_id, stars=rating.stars)
        db.add(db_rating)

    db.commit()
    db.refresh(db_rating)
    return db_rating

def get_average_rating(db: Session, lesson_id: int):
    avg = db.query(func.avg(Rating.stars)).filter(Rating.lesson_id == lesson_id).scalar()
    return round(avg or 0.0, 2)