from src.app.constants import DATABASE
from pymongo import MongoClient

class PondRepository:
    def __init__(self):
        DB: DATABASE = DATABASE()
        self.client = MongoClient(DB.URI)
        self.db = self.client[DB.NAME]
        self.pond = self.db[DB.COLLECTIONS.POND]

    def insert_one(self, data):
        return self.pond.insert_one(data)
    
    def insert_many(self, documents):
        return self.pond.insert_many(documents)
    
    def find(self, filter):
        return self.pond.find(filter)
    
    def find_one(self, filter):
        return self.pond.find_one(filter)
    
    def delete_one(self, filter):
        return self.pond.delete_one(filter)
    
    def delete_many(self, filter):
        return self.pond.delete_many(filter)
    
    def update_one(self, filter, setPayload):
        return self.pond.update_one(filter, setPayload)
    
    def update_many(self, filter, setPayload):
        return self.pond.update_many(filter, setPayload)