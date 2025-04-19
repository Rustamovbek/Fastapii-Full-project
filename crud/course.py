from sqlalchemy.orm import Session
from models.course import Course
from schemas.course import CourseCreate, CourseUpdate

def create_course(db: Session, course: CourseCreate, author_id: int):
    db_course = Course(
        title=course.title,
        description=course.description,
        author_id=author_id
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

def get_all_courses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Course).offset(skip).limit(limit).all()

def update_course(db: Session, course_id: int, course: CourseUpdate):
    db_course = get_course(db, course_id)
    if not db_course:
        return None
    db_course.title = course.title
    db_course.description = course.description
    db.commit()
    db.refresh(db_course)
    return db_course

def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    if not db_course:
        return None
    db.delete(db_course)
    db.commit()
    return db_course
