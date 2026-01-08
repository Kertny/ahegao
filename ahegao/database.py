from sqlalchemy import create_engine, MetaData, String, DateTime, func, Boolean
from structure import Settings
import os
import aiosqlite
import datetime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker

database = os.getenv("DATABASE")

engine = create_engine(database)
Session = sessionmaker(bind=engine)
Metadata = MetaData()

class Ahegao(DeclarativeBase):
    pass

class Users(Ahegao):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True) # sa.Column(sa.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255)) # sa.Column(sa.String(255))
    mail: Mapped[str] = mapped_column(String(255), unique=True, index=True) # sa.Column(sa.String(255), unique=True, index=True)
    date: Mapped[datetime] = mapped_column(DateTime) #  sa.Column(sa.DateTime)

class Question(Ahegao):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now()) # sa.Column(sa.DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now())
    title: Mapped[str] = mapped_column(String(255)) # sa.Column(sa.String(255))
    metrics: Mapped[bool] = mapped_column(Boolean) # sa.Column(sa.Boolean)

def create_tables(engine = engine):
    Ahegao.metadata.create_all(engine)

def drop_tables(engine = engine):
    Ahegao.metadata.drop_all(engine)
