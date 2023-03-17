from src.app.constants import DATABASE
from pymongo import MongoClient

class UserRepository:
    def __init__(self):
        DB: DATABASE = DATABASE()
        self.client = MongoClient(DB.URI)
        self.db = self.client[DB.NAME]
        self.user = self.db[DB.COLLECTIONS.USER]

    def insert_one(self, data):
        return self.user.insert_one(data)
    
    def insert_many(self, documents):
        return self.user.insert_many(documents)
    
    def find(self, filter):
        return self.user.find(filter)
    
    def find_one(self, filter):
        return self.user.find_one(filter)
    
    def delete_one(self, filter):
        return self.user.delete_one(filter)
    
    def delete_many(self, filter):
        return self.user.delete_many(filter)
    
    def update_one(self, filter, setPayload):
        return self.user.update_one(filter, setPayload)
    
    def update_many(self, filter, setPayload):
        return self.user.update_many(filter, setPayload)