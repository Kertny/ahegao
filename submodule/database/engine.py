from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy import create_engine

class BaseConn():
    pass

class Users(BaseConn):
    pass

engine = create_engine(url="postgresql+psycopg2://postgres:tttest26@localhost:5432/")
