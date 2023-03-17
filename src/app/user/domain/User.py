class User:
    def __init__(self, payload):
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
        return response