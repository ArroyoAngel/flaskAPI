class Pond:
    def __init__(self, payload):
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
        return response