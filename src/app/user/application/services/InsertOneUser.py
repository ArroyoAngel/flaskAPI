from src.app.user.infraestructure.DataBaseAdapter import UserRepository
from bson.json_util import _json_convert

class InsertOneUser:
    def __init__(self):
        self.repository = UserRepository()

    def insertOneUser(self, user):
        response = self.repository.insert_one(user)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": _json_convert(response.inserted_id)["$oid"]
        }