from src.app.constants import DATABASE
from pymongo import MongoClient

class AccountRepository:
    def __init__(self):
        DB: DATABASE = DATABASE()
        self.client = MongoClient(DB.URI)
        self.db = self.client[DB.NAME]
        self.account = self.db[DB.COLLECTIONS.ACCOUNT]

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