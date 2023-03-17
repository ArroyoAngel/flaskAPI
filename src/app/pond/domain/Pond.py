from bson import ObjectId

class Pond:
    def __init__(self, payload):
        self._id = str(payload["_id"]) if "_id" in payload else None
        self.name = payload["name"]
        self.zone = payload["zone"]
        self.width = payload["width"]
        self.height = payload["height"]
        self.depth = payload["depth"]
    
    def toDict(self):
        response = {
            "name": self.name,
            "zone": self.zone,
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
        }
        if self._id != None:
            response["_id"] = self._id
        return response
    
    def toBson(self):
        response = {
            "name": self.name,
            "zone": self.zone,
            "width": self.width,
            "height": self.height,
            "depth": self.depth,
        }
        if self._id != None:
            response["_id"] = ObjectId(self._id)
        return response