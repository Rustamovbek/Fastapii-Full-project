from typing import Annotated
from datetime import timedelta
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from routers.lesson import router as lesson_router
from routers.course import router as course_router
from routers.rating import router as rating_router
from routers.comment import router as comment_router
from database import engine, SessionLocal
from core.auth import (
    get_current_user,
    authenticate_user,
    create_access_token,
    bcrypt_context,
)
from models import user
from models.user import User
from models.base import BaseResponse
from schemas.login import LoginRequest
from schemas.user import CreateUserFrom, Token

app = FastAPI()

user.Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


DBSessionDep = Annotated[Session, Depends(get_db)]
CurrentUserDep = Annotated[dict, Depends(get_current_user)]

router = APIRouter(
    prefix="/auth",
    tags=["Auth-API"]
)


@router.get("/user", status_code=status.HTTP_200_OK)
async def get_authenticated_user(
        current_user: CurrentUserDep
):
    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Auth failed"
        )
    return {"user": current_user}  # noqa


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BaseResponse)
async def register_user(
        db: DBSessionDep,
        create_user_request: CreateUserFrom
):
    existing_user = db.query(User).filter(User.email == create_user_request.email).first()  # noqa
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    new_user = User(
        full_name=create_user_request.full_name,
        email=create_user_request.email,  # noqa
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=create_user_request.is_active,
        is_admin=create_user_request.is_admin
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    data = {
        "fullname": new_user.full_name,
        "email": new_user.email,
        "password": new_user.hashed_password,
        "is_active": new_user.is_active,
        "is_admin": new_user.is_admin
    }
    return BaseResponse(data=data)


@router.post("/token", response_model=Token)
async def login_for_access_token(
        form_data: LoginRequest,
        db: DBSessionDep
):
    auth_user = authenticate_user(form_data.email, form_data.password, db)
    if not auth_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email or password incorrect"
        )

    token = create_access_token(
        email=auth_user.email,
        user_id=auth_user.id,
        expires_delta=timedelta(minutes=20)
    )
    return {"access_token": token, "token_type": "Bearer"}


app.include_router(router)
app.include_router(course_router)
app.include_router(lesson_router)
app.include_router(comment_router)
app.include_router(rating_router)