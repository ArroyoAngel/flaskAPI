from src.app.pond.infraestructure.DataBaseAdapter import PondRepository
from bson.json_util import _json_convert

class InsertOnePond:
    def __init__(self):
        self.repository = PondRepository()

    def insertOnePond(self, pond):
        response = self.repository.insert_one(pond)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": _json_convert(response.inserted_id)["$oid"]
        }