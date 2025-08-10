from structure import UserSchema

users = ["Kim", "Klav", "Kum"]

def verified_user(user):
    if user.name in users:
        return {f'user not validate'}
    else:
        users.append(user.name)
        return {f'user add list'}
