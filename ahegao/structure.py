from pydantic import BaseModel, Field, EmailStr
from datetime import date

class UserSchema(BaseModel):
    username: str
    mail: EmailStr
    date: date

class AddintionalSchema(UserSchema):
    id: int

class Settings(BaseModel):
    db_url: str
    rabbit_url: str
