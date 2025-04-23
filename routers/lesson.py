from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from crud import lesson as crud_lesson
from schemas.lesson import LessonCreate, LessonUpdate, LessonOut
from core.dependencies import DBSessionDep, CurrentUserDep, db_dependencies

router = APIRouter(
    prefix="/lessons",
    tags=["Lessons-API"]
)

@router.post("/", response_model=LessonOut, status_code=HTTP_201_CREATED)
def create_lesson(
    lesson: LessonCreate,
    db: DBSessionDep,
    current_user: CurrentUserDep
):
    return crud_lesson.create_lesson(db, lesson, author_id=current_user["id"])


@router.get("/{lesson_id}", response_model=LessonOut)
def read_lesson(
    lesson_id: int,
    db: DBSessionDep
):
    db_lesson = crud_lesson.get_lesson(db, lesson_id)
    if not db_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return db_lesson


@router.get("/", response_model=List[LessonOut])
def read_lessons(
    skip: int = 0,
    limit: int = 10,
    db: Session = db_dependencies
):
    return crud_lesson.get_lessons(db, skip, limit)


@router.put("/{lesson_id}", response_model=LessonOut)
def update_lesson(
    lesson_id: int,
    lesson: LessonUpdate,
    db: DBSessionDep,
    current_user: CurrentUserDep
):
    db_lesson = crud_lesson.get_lesson(db, lesson_id)
    if not db_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    if db_lesson.author_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to update this lesson")

    updated = crud_lesson.update_lesson(db, lesson_id, lesson)
    if not updated:
        raise HTTPException(status_code=400, detail="Update failed")

    return updated


@router.delete("/{lesson_id}", status_code=HTTP_204_NO_CONTENT)
def delete_lesson(
    lesson_id: int,
    db: DBSessionDep,
    current_user: CurrentUserDep
):
    db_lesson = crud_lesson.get_lesson(db, lesson_id)
    if not db_lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")

    if db_lesson.author_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this lesson")

    deleted = crud_lesson.delete_lesson(db, lesson_id)
    if not deleted:
        raise HTTPException(status_code=400, detail="Delete failed")
    return