from pydantic import BaseModel, Field, EmailStr
from datetime import date

class UserSchema(BaseModel):
    username: str

class AddintionalSchema(UserSchema):
    id: int
    mail: EmailStr
    date: date

class Settings(BaseModel):
    db_url: str
    rabbit_url: str
