from database import new_session, Users
from structure import UserSchema
from sqlalchemy import select

class BaseManipulation:
    @classmethod
    async def add_one(cls, user: UserSchema):
        async with new_session() as session:
            user_dict = user.model_dump()
            date = Users(**user_dict)
            session.add(date)
            await session.flush()
            await session.commit()
            return date.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(Users)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models

    @classmethod
    async def get_user(cls, date: UserSchema):
        async with new_session() as session:
            query = select(Users).filter_by(username=date)
            result = await session.execute(query)
            return result.scalars().all()