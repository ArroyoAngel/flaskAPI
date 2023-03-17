from src.app.pond.domain.Pond import Pond
from src.app.pond.infraestructure.DataBaseAdapter import PondRepository
from bson import ObjectId

class GetPond:
    def __init__(self):
        self.repository = PondRepository()

    def getPonds(self, filter={}):
        if filter !=None and "_id" in filter:
            filter = { "_id": ObjectId(filter["id"]) }
        response = list(self.repository.find(filter))
        result = []
        for pond in response:
            result.append(Pond(pond).toDict())
        return result
    
    def getById(self, id):
        response = list(self.repository.find({
            "_id": ObjectId(id)
        }))
        pond = response[0]
        result = Pond(pond).toDict()
        return result
    
    def filterPonds(self, key, value):
        filter = {}
        filter[key] = value
        response = list(self.repository.find(filter))
        result = []
        for pond in response:
            result.append(Pond(pond).toDict())
        
        return result
            