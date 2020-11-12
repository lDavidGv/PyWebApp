import pymongo
from pymongo import MongoClient
import bcrypt

class LoginModel:
    def __init__(self):
        print("entra al metodo")
        self.client = MongoClient()
        self.db = self.client.PetPin
        self.Users = self.db.users

    def cu(self, data):
        print("holasd")
        user = self.Users.find_one({"username": data.username})
        print(user)

        if user:
            if bcrypt.checkpw(data.password.encode(), user["password"]):
                return user
            else:
                return False

        else:
            return False
