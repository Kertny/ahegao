from fastapi import FastAPI
from labub import verified_user

app = FastAPI()

@app.get("/")
def home_page(home: str):
    home = "hello my friend"
    return {"data": home}

@app.post("/useradd")
def user_add(user: str):
    verified_user(user)
    