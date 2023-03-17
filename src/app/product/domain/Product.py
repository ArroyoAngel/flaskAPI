from bson import ObjectId

class Product:
    def __init__(self, payload):
        self._id = str(payload["_id"]) if "_id" in payload else None
        self.name = payload["name"]
        self.type = payload["type"]
        self.detail = payload["detail"]
        self.amount = payload["amount"]
        self.measure = payload["measure"]
    
    def toDict(self):
        response = {
            "name": self.name,
            "type": self.type,
            "detail": self.detail,
            "amount": self.amount,
            "measure": self.measure,
        }
        if self._id != None:
            response["_id"] = self._id
        return response
    
    def toBson(self):
        response = {
            "name": self.name,
            "type": self.type,
            "detail": self.detail,
            "amount": self.amount,
            "measure": self.measure,
        }
        if self._id != None:
            response["_id"] = ObjectId(self._id)
        return response