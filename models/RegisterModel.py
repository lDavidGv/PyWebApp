import pymongo
from pymongo import MongoClient
import bcrypt

class RegistrationModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.PetPin
        self.Users = self.db.users

    def inset_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(),bcrypt.gensalt())
        id = self.Users.insert({"username": data.username, "name": data.name, "password": hashed, "email": data.email})
        myuser = self.Users.find_one({"username": data.username})

        if bcrypt.checkpw("avocado1".encode(),myuser["password"]):
            print("this matches")