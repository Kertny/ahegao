from sqlalchemy import create_engine
from structure import Settings
import os
import aiosqlite
import datetime
import sqlalchemy as sa
from sqlalchemy import schema, Column, Integer, String, Table, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker

database = "sqlite:///base.db"

engine = create_engine(database)
Session = sessionmaker(bind=engine)
Metadata = sa.MetaData()
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
    created_at = sa.Column(sa.DateTime, server_default=func.now())
    updated_at = sa.Column(sa.DateTime, server_default=func.now(), server_onupdate=func.now())
    title = sa.Column(sa.String(255))
    metrics = sa.Column(sa.Boolean)

def create_tables(engine = engine):
    Ahegao.metadata.create_all(engine)

def drop_tables(engine = engine):
    Ahegao.metadata.drop_all(engine)
