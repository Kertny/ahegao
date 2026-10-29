from fastapi import FastAPI
from contextlib import asynccontextmanager
# from database.engine import engine as db


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     db.connect()
#     yield
#     db.disconect()


app = FastAPI() # lifespan=lifespan

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5050", "http://127.0.0.1:5050"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get('/key')
def get_secret(key: str):
    print(key)
    return {'data': 'ok'}

@app.get('/date')
def get_date(date: str):
    print(date)
    return {'data': 'ok'}

@app.get('/time')
def get_date(time: str):
    print(time)
    return {'data': 'ok'}

@app.get('/result')
def get_result_message(result: str):
    print(result)
    return {'data': 'ok'}