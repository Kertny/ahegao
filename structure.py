from pydantic import BaseModel, Field, EmailStr
from datetime import date

class UserSchema(BaseModel):
    user: str
    mail: EmailStr
    date: date

