#from app.models.user import User
from pymongo import MongoClient

DB_NAME = "flaskapi"
USER_DB = "luis"
USER_PWD = "luis123"
URL = f"mongodb://{USER_DB}:{USER_PWD}@localhost:27017"

class ActivityRepository:
    def __init__(self, MONGO_URI=f'{URL}/{DB_NAME}', MONGO_DB="flaskapi"):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.activity = self.db.activity

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