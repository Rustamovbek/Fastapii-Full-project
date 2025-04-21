from sqlalchemy.orm import Session
from models.lesson import Lesson
from schemas.lesson import LessonCreate, LessonUpdate
from typing import Optional, List

def get_lesson(db: Session, lesson_id: int) -> Optional[Lesson]:
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()

def get_lessons(db: Session, skip: int = 0, limit: int = 10) -> List[Lesson]:
    return db.query(Lesson).offset(skip).limit(limit).all()

def create_lesson(db: Session, lesson: LessonCreate, author_id: int) -> Lesson:
    db_lesson = Lesson(
        course_id=lesson.course_id,
        title=lesson.title,
        video_url=str(lesson.video_url) if lesson.video_url else None,
        content=lesson.content,
        author_id=author_id
    )
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def update_lesson(db: Session, lesson_id: int, lesson: LessonUpdate):
    db_lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not db_lesson:
        return None

    db_lesson.title = lesson.title
    db_lesson.video_url = str(lesson.video_url)
    db_lesson.content = lesson.content

    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def delete_lesson(db: Session, lesson_id: int) -> Optional[Lesson]:
    db_lesson = get_lesson(db, lesson_id)
    if not db_lesson:
        return None

    db.delete(db_lesson)
    db.commit()
    return db_lesson
