#from app.models.user import User
from pymongo import MongoClient

URL = "mongodb://localhost:27017"

class AccountRepository:
    def __init__(self, MONGO_URI='mongodb://localhost:27017', MONGO_DB="flaskapi"):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.account = self.db.account

    def insert_one(self, data):
        return self.account.insert_one(data)
    
    def insert_many(self, documents):
        return self.account.insert_many(documents)
    
    def find(self, filter):
        return self.account.find(filter)
    
    def find_one(self, filter):
        return self.account.find_one(filter)
    
    def delete_one(self, filter):
        return self.account.delete_one(filter)
    
    def delete_many(self, filter):
        return self.account.delete_many(filter)
    
    def update_one(self, filter, setPayload):
        return self.account.update_one(filter, setPayload)
    
    def update_many(self, filter, setPayload):
        return self.account.update_many(filter, setPayload)