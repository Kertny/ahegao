from database import Session, Users, Question
from structure import UserSchema, AnalyticsSchema
from sqlalchemy import select

class BaseManipulation:
    @classmethod
    def add_one(cls, user: UserSchema):
        with Session() as session:
            user_dict = user.model_dump()
            data = Users(**user_dict)
            session.add(data)
            session.commit()
            return data.id

    @classmethod
    def get_all(cls):
        with Session() as session:
            query = select(Users)
            result = session.execute(query)
            user_models = result.scalars().all()
            return user_models

    @classmethod
    def get_user(cls, date: UserSchema):
        with Session() as session:
            query = select(Users).filter_by(username=date)
            result = session.execute(query)
            return result.scalars().all()
        
    @classmethod
    def question_create(cls, data: AnalyticsSchema):
        with Session() as session:
            data_dict = data.model_dump()
            inter = Question(**data_dict)
            session.add(inter)
            session.commit()
            return inter.id
        
    @classmethod
    def question_search(cls, id: int):
        with Session() as session:
            query = select(Question).filter_by(id=id)
            result = session.execute(query)
            return result.scalars().all()
