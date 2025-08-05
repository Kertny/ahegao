from structure import UserSchema

def app():
    data = {
        "user": "Kuk",
        "mail": "my@mail.ru",
        "date": "2000-04-09",
    }

    user = UserSchema(**data)

    print(user)