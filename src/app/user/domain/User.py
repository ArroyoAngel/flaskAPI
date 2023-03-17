from bson import ObjectId

class User:
    def __init__(self, payload):
        self._id = str(payload["_id"]) if "_id" in payload else None
        self.name = payload["name"]
        self.phone = payload["phone"]
        self.credential = payload["credential"]
        self.role = payload["role"]
        self.username = payload["username"]
    
    def toDict(self):
        response = {
            "name": self.name,
            "phone": self.phone,
            "credential": self.credential,
            "role": self.role,
            "username": self.username,
        }
        if self._id != None:
            response["_id"] = self._id
        return response
    
    def toBson(self):
        response = {
            "name": self.name,
            "phone": self.phone,
            "credential": self.credential,
            "role": self.role,
            "username": self.username,
        }
        if self._id != None:
            response["_id"] = ObjectId(self._id)
        return response