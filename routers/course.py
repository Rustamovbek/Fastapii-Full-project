from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT

from crud import course as crud_course
from schemas.course import CourseCreate, CourseUpdate, CourseOut
from core.auth import get_current_user, db_dependency

router = APIRouter(
    prefix="/courses",
    tags=["Courses-API"]
)


@router.post("/", response_model=CourseOut, status_code=HTTP_201_CREATED)
def create_course(
    course: CourseCreate,
    db: Session = db_dependency,
    current_user: dict = Depends(get_current_user)
):
    return crud_course.create_course(db, course, author_id=current_user["id"])


@router.get("/{course_id}", response_model=CourseOut)
def read_course(
    course_id: int,
    db: Session = db_dependency
):
    db_course = crud_course.get_course(db, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course


@router.get("/", response_model=List[CourseOut])
def read_courses(
    skip: int = 0,
    limit: int = 10,
    db: Session = db_dependency
):
    return crud_course.get_all_courses(db, skip, limit)


@router.put("/{course_id}", response_model=CourseOut)
def update_course(
    course_id: int,
    course: CourseUpdate,
    db: Session = db_dependency,
    current_user: dict = Depends(get_current_user)
):
    db_course = crud_course.get_course(db, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    if db_course.author_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to update this course")

    updated_course = crud_course.update_course(db, course_id, course)
    if not updated_course:
        raise HTTPException(status_code=400, detail="Update failed")
    return updated_course


@router.delete("/{course_id}", status_code=HTTP_204_NO_CONTENT)
def delete_course(
    course_id: int,
    db: Session = db_dependency,
    current_user: dict = Depends(get_current_user)
):
    db_course = crud_course.get_course(db, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")

    if db_course.author_id != current_user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this course")

    deleted = crud_course.delete_course(db, course_id)
    if not deleted:
        raise HTTPException(status_code=400, detail="Delete failed")
    return  # No content (204)
