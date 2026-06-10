from pydantic import BaseModel, Field, EmailStr


import random


class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000)
    name: str
    age: int = Field(ge=0)
