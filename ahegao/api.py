from fastapi import FastAPI, APIRouter, Depends 
from typing import Annotated
from contextlib import asynccontextmanager
from repodos import BaseManipulation
from app import log
from database import create_tables, drop_tables
from rabbit import node
from structure import UserSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    log.warning("Databese ready to work")
    yield

router = APIRouter()

@router.get("/")
async def home_page():
    home = "hello my friend"
    return {"data": home}

@router.post("/useradd")
async def user_add(
    username: Annotated[UserSchema, Depends()]
):
    user_id = await BaseManipulation.add_one(username)
    return {"ok": True, "user_id": user_id}

@router.get("/users")
async def get_users():
    user_id = await BaseManipulation.get_all()
    return {"data": user_id}

@router.get("/abonent")
async def get_user(
    username: str
):
    try:
        user = await BaseManipulation.get_user(username)
        return user
    except Exception as ex:
        raise ex

app = FastAPI(lifespan=lifespan)
app.include_router(node)
app.include_router(router)
