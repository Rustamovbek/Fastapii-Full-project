from pydantic import BaseModel, EmailStr, ConfigDict


class CreateUserFrom(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    is_active: bool
    is_admin: bool

class UserOut(BaseModel):
    id: int
    full_name: str

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str