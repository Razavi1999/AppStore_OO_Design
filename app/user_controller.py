from user import User
from developer import Developer

class UserController:
    """docstring for UserController."""

    def __init__(self):
        self.users = []

    def signUp(self, email , name , image):
        user = User(email , name , image)
        print(f'New User {user.name} created.')
        self.users.append(user)
        return user

    def create_developer(self, name, icon):
        return Developer(name, icon)

