from pydantic import BaseModel, Field, EmailStr
from datetime import date

class UserSchema(BaseModel):
    name: str
    mail: EmailStr
    date: date
    