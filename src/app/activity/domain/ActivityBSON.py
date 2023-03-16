class ActivityBSON:
    def __init__(self, payload):
        self.id = payload["_id"]
        self.type = payload["type"]
        self.date = payload["date"]
        self.detail = payload["detail"]

    def toDict(self):
        response = {
            "id": self.id["$oid"],
            "type": self.type,
            "date": self.date,
            "detail": self.detail,
        }
        return response