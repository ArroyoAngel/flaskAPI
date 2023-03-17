from src.app.user.domain.UserBSON import UserBSON
from src.app.user.infraestructure.DataBaseAdapter import UserRepository
from bson.json_util import _json_convert

class InsertManyUsers:
    def __init__(self):
        self.repository = UserRepository()

    def insertManyUsers(self, documents) -> list[UserBSON]:
        response = self.repository.insert_many(documents)
        _json_response = _json_convert(response.inserted_ids)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": [
                str(id["$oid"]) for id in _json_response
            ]
        }