from src.app.constants import DATABASE
from pymongo import MongoClient

class ProductRepository:
    def __init__(self):
        DB: DATABASE = DATABASE()
        self.client = MongoClient(DB.URI)
        self.db = self.client[DB.NAME]
        self.product = self.db[DB.COLLECTIONS.PRODUCT]

    def insert_one(self, data):
        return self.product.insert_one(data)
    
    def insert_many(self, documents):
        return self.product.insert_many(documents)
    
    def find(self, filter):
        return self.product.find(filter)
    
    def find_one(self, filter):
        return self.product.find_one(filter)
    
    def delete_one(self, filter):
        return self.product.delete_one(filter)
    
    def delete_many(self, filter):
        return self.product.delete_many(filter)
    
    def update_one(self, filter, setPayload):
        return self.product.update_one(filter, setPayload)
    
    def update_many(self, filter, setPayload):
        return self.product.update_many(filter, setPayload)