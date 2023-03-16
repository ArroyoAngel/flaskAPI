class Activity:
    def __init__(self, payload):
        self.type = payload["type"]
        self.date = payload["date"]
        self.detail = payload["detail"]
    
    def toDict(self):
        response = {
            "type": self.type,
            "date": self.date,
            "detail": self.detail,
        }
        return response