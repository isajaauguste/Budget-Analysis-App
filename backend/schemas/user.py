from pydantic import BaseModel, EmailStr, Field, model_validator
from pydantic_core import PydanticCustomError


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)
    repeat_password: str = Field(min_length=6, max_length=72)

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.repeat_password:
            raise PydanticCustomError("password_mismatch", "Passwords do not match")
        return self


class UserResponse(BaseModel):
    user_id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    login: str
    password: str
