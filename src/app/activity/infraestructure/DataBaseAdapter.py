from src.app.constants import DATABASE
from pymongo import MongoClient

class ActivityRepository:
    def __init__(self):
        DB: DATABASE = DATABASE()
        self.client = MongoClient(DB.URI)
        self.db = self.client[DB.NAME]
        self.activity = self.db[DB.COLLECTIONS.ACTIVITY]

    def insert_one(self, data):
        return self.activity.insert_one(data)
    
    def insert_many(self, documents):
        return self.activity.insert_many(documents)
    
    def find(self, filter):
        return self.activity.find(filter)
    
    def delete_one(self, filter):
        return self.activity.delete_one(filter)
    
    def delete_many(self, filter):
        return self.activity.delete_many(filter)
    
    def update_one(self, filter, setPayload):
        return self.activity.update_one(filter, setPayload)
    
    def update_many(self, filter, setPayload):
        return self.activity.update_many(filter, setPayload)