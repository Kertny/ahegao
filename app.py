import uvicorn
import logging
from labub import verified_user
from structure import UserSchema

UserData = {
    "name": "Kert",
    "mail": "fufil@mail.ru",
    "date": "2002-04-13",
}

log = logging.getLogger()

user = UserSchema(**UserData)

if __name__ == '__main__':
    log.warning("app start")
    uvicorn.run('api:app', port=5050, log_level="info")
    verified_user(user)
    log.warning("app stoped")