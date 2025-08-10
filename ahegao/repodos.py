from database import new_session, UserORM
from structure import UserSchema
from sqlalchemy import select

class BaseManipulation:
    @classmethod
    async def add_one(cls, user: UserSchema):
        async with new_session() as session:
            user_dict = user.model_dump()
            date = UserORM(**user_dict)
            session.add(date)
            await session.flush()
            await session.commit()
            return date.id

    @classmethod
    async def get_all(cls):
        async with new_session() as session:
            query = select(UserORM)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models
