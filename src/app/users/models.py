from datetime import timedelta
from bson.json_util import _json_convert, dumps
from bson.objectid import ObjectId
from flask import request
from app.db import mongo
import json

def response(message, payload, status=200, id=""):
    return {
        "status": status,
        "message": message,
        "payload": payload,
        "id": id,
    }

class Users():
    def __init__(self):
        self.data = []
        self.get()
        pass
    
    def get(self)->object:
        response = mongo.db.users.find()
        response = _json_convert(response)

        result = []
        for u in response:
            result.append(User(u))
        self.data = result
        return result

    def filter(self, query)->object:
        response = mongo.db.users.find(query)
        response = _json_convert(response)
        self.users = response
        return response 
    
    def find(self, id)->object:
        objInstance = ObjectId(id)
        response = mongo.db.users.find_one({"_id": objInstance})
        result = _json_convert(response)
        return result

    def add(self, data):
        name = data["name"]
        lastname = data["lastname"]
        phone = data["phone"]
        birthdate = data["birthdate"]
        nit = data["nit"]
        
        inserted = mongo.db.users.insert_one({ "name": name,"lastname": lastname, "phone": phone, "birthdate": birthdate, "nit": nit })
        id = _json_convert(inserted.inserted_id)
        self.data.append(User({ "_id": id,"name": name,"lastname": lastname, "phone": phone, "birthdate": birthdate, "nit": nit }))
        return response( "Cuenta creada Exitosamente", { 
            "ID": id["$oid"],"Name": name,"Lastname": lastname, "Phone": phone, "Birthdate": birthdate, "NIT": nit 
        }, 200, id["$oid"] )

    def update(self, query, data)->object:
        mongo.db.users.update_one(query, {
            "$set": data
        })
        resolve = User(data)
        return {
            "status": 200,
            "message": "SUCCESS"
        }

    def delete(self, query)->object:
        mongo.db.users.delete_one(query)
        return {
            "status": 200,
            "message": "SUCCESS"
        }
    
def User(data):
    user = {}
    for field in data:
        if(field=="_id"):           user["id"] = data["_id"]["$oid"]
        elif(field=="name"):        user["name"] = data["name"]
        elif(field=="lastname"):    user["lastname"] = data["lastname"]
        elif(field=="phone"):       user["phone"] = data["phone"]
        elif(field=="birthdate"):   user["birthdate"] = data["birthdate"]
        elif(field=="nit"):         user["nit"] = data["nit"]
    
    return user