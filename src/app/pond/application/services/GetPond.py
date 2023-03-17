from src.app.pond.domain.PondBSON import PondBSON
from src.app.pond.infraestructure.DataBaseAdapter import PondRepository
from bson.json_util import _json_convert
from bson import ObjectId

class GetPond:
    def __init__(self):
        self.repository = PondRepository()

    def getPonds(self, filter={}) -> list[PondBSON]:
        if filter !=None and "id" in filter:
            filter = { "_id": ObjectId(filter["id"]) }
        response = _json_convert(self.repository.find(filter))
        result = []
        for pond in response:
            result.append(PondBSON(pond).toDict())
        return result
    
    def getById(self, id) -> list[PondBSON]:
        response = _json_convert(self.repository.find({
            "_id": ObjectId(id)
        }))
        result = PondBSON(response[0]).toDict()
        return result
    
    def filterPonds(self, key, value) -> list[PondBSON]:
        filter = {}
        filter[key] = value
        response = _json_convert(self.repository.find(filter))
        result = []
        for pond in response:
            result.append(PondBSON(pond).toDict())
        
        return result
            