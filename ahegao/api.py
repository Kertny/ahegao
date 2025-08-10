from fastapi import FastAPI, Depends
from typing import Annotated
from contextlib import asynccontextmanager
from repodos import BaseManipulation
from app import log
from database import create_tables, drop_tables
from structure import UserSchema

@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    await create_tables()
    log.warning("Databese ready to work")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def home_page():
    home = "hello my friend"
    return {"data": home}

@app.post("/useradd")
async def user_add(
    username: Annotated[UserSchema, Depends()]
):
    user_id = await BaseManipulation.add_one(username)
    return {"ok": True, "user_id": user_id}

@app.get("/users")
async def get_users():
    user_id = await BaseManipulation.get_all()
    return {"data": user_id}
