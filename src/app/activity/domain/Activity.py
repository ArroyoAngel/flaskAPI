from bson import ObjectId
class Activity:
    def __init__(self, payload):
        self._id = str(payload["_id"]) if "_id" in payload else None
        self.type = payload["type"]
        self.date = payload["date"]
        self.detail = payload["detail"]
        self._pond = str(payload["_pond"])
    
    def toDict(self):
        response = {
            "type": self.type,
            "date": self.date,
            "detail": self.detail,
            "_pond": self._pond,
        }
        if self._id != None:
            response["_id"] = self._id
        return response
    
    def toBson(self):
        response = {
            "type": self.type,
            "date": self.date,
            "detail": self.detail,
            "_pond": ObjectId(self._pond),
        }
        if self._id != None:
            response["_id"] = ObjectId(self._id)
        return response