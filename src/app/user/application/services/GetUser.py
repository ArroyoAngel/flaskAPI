from src.app.user.domain.User import User
from src.app.user.infraestructure.DataBaseAdapter import UserRepository
from bson import ObjectId

class GetUser:
    def __init__(self):
        self.repository = UserRepository()

    def getUsers(self, filter={}):
        if filter !=None and "id" in filter:
            filter = { "_id": ObjectId(filter["id"]) }
        response = list(self.repository.find(filter))
        result = []
        for user in response:
            result.append(User(user).toDict())
        return result
    
    def getById(self, id):
        response = list(self.repository.find({
            "_id": ObjectId(id)
        }))
        user = response[0]
        result = User(user).toDict()
        return result
    
    def filterUsers(self, key, value):
        filter = {}
        filter[key] = value
        response = list(self.repository.find(filter))
        result = []
        for user in response:
            result.append(User(user).toDict())
        
        return result
            