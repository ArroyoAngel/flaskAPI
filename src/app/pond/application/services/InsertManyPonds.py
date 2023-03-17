from src.app.pond.domain.PondBSON import PondBSON
from src.app.pond.infraestructure.DataBaseAdapter import PondRepository
from bson.json_util import _json_convert

class InsertManyPonds:
    def __init__(self):
        self.repository = PondRepository()

    def insertManyPonds(self, documents) -> list[PondBSON]:
        response = self.repository.insert_many(documents)
        _json_response = _json_convert(response.inserted_ids)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": [
                str(id["$oid"]) for id in _json_response
            ]
        }