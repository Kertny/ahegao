from fastapi import FastAPI, APIRouter, Depends 
from typing import Annotated
from contextlib import asynccontextmanager
from repodos import BaseManipulation
from app import log
from database import create_tables, drop_tables
# from rabbit import node
from structure import UserSchema, AnalyticsSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    drop_tables()
    create_tables()
    log.warning("Databese ready to work")
    yield

router = APIRouter()

@router.get("/")
def home_page():
    home = "hello my friend"
    return {"data": home}

# @router.post("/useradd")
# def user_add(
#     username: Annotated[UserSchema, Depends()]
# ):
#     user_id = BaseManipulation.add_one(username)
#     return {"ok": True, "user_id": user_id}

# @router.get("/users")
# def get_users():
#     user_id = BaseManipulation.get_all()
#     return {"data": user_id}

# @router.get("/abonent")
# def get_user(
#     username: str
# ):
#     try:
#         user = BaseManipulation.get_user(username)
#         return user
#     except Exception as ex:
#         raise ex
    
# @router.post("/question")
# def question_integrate(
#     data_inc: Annotated[AnalyticsSchema, Depends()]
# ):
#     upload = BaseManipulation.question_create(data_inc)
#     return {"data": upload}

# @router.get("/getquestion")
# def get_question(id: int):
#     data = BaseManipulation.question_search(id)
#     return data

# @router.post("/qmodify")
# def question_modify(id: int):
#     data = BaseManipulation.question_modify(id)
#     return data

@router.get('/key')
def get_secret(key: str):
    print(key)
    return {'data': 'ok'}

@router.get('/date')
def get_date(date: str):
    print(date)
    return {'data': 'ok'}

@router.get('/time')
def get_date(time: str):
    print(time)
    return {'data': 'ok'}

@router.get('/result')
def get_result_message(result: str):
    print(result)
    return {'data': 'ok'}


app = FastAPI(lifespan=lifespan)
# app.include_router(node)
app.include_router(router)
