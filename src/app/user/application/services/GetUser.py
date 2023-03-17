from src.app.user.domain.UserBSON import UserBSON
from src.app.user.infraestructure.DataBaseAdapter import UserRepository
from bson.json_util import _json_convert
from bson import ObjectId

class GetUser:
    def __init__(self):
        self.repository = UserRepository()

    def getUsers(self, filter={}) -> list[UserBSON]:
        if "id" in filter:
            filter = { "_id": ObjectId(filter["id"]) }
        response = _json_convert(self.repository.find(filter))
        result = []
        for user in response:
            result.append(UserBSON(user).toDict())
        return result
    
    def getById(self, id) -> list[UserBSON]:
        response = _json_convert(self.repository.find({
            "_id": ObjectId(id)
        }))
        result = UserBSON(response[0]).toDict()
        return result
    
    def filterUsers(self, key, value) -> list[UserBSON]:
        filter = {}
        filter[key] = value
        response = _json_convert(self.repository.find(filter))
        result = []
        for user in response:
            result.append(UserBSON(user).toDict())
        
        return result
            