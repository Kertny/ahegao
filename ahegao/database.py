from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from pydantic import EmailStr, Field
from structure import Settings
import os
import aiosqlite
from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

endpointBase = Settings.DB_URL = os.getenv("DATABASE")

engine = create_async_engine(
    endpointBase
)

new_session = async_sessionmaker(engine, expire_on_commit=False)

class Model(DeclarativeBase):
    pass

class UserORM(Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    mail: Mapped[EmailStr] = Field(unique=True, index=True)
    date: Mapped[date]


async def create_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Model.metadata.create_all)

async def drop_tables():
    async with engine.begin() as connect:
        await connect.run_sync(Model.metadata.drop_all)
