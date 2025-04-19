from pydantic import BaseModel, EmailStr


class CreateUserFrom(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    is_active: bool
    is_admin: bool

class UserOut(BaseModel):
    id: int
    full_name: str

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
