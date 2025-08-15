from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pydantic import EmailStr, Field
from structure import Settings
import os
import aiosqlite
import datetime
import sqlalchemy as sa
from sqlalchemy import schema, Column, Integer, String, Table, DateTime
from sqlalchemy.orm import declarative_base

endpointBase = Settings.DB_URL = os.getenv("DATABASE")

engine = create_async_engine(endpointBase)

new_session = async_sessionmaker(engine, expire_on_commit=False)

Ahegao = declarative_base()

class Users(Ahegao):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(255))
    mail = sa.Column(sa.String(255), unique=True, index=True)
    date = sa.Column(sa.DateTime)

class Question(Ahegao):
    __tablename__ = "question"

    id = sa.Column(sa.Integer, primary_key=True)
    created_at = sa.Column(sa.DateTime)

async def create_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Ahegao.metadata.create_all)

async def drop_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Ahegao.metadata.drop_all)
