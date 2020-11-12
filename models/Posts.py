import pymongo
from pymongo import MongoClient
class Posts:
    def __init__(self):
        print("entra al metodo")
        self.client = MongoClient()
        self.db = self.client.PetPin
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):
        insert = self.Posts.insert({"username": data.username, "content": data.content})
        return True

