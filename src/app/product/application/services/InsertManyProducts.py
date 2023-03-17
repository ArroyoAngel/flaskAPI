from src.app.product.infraestructure.DataBaseAdapter import ProductRepository
from bson.json_util import _json_convert

class InsertManyProducts:
    def __init__(self):
        self.repository = ProductRepository()

    def insertManyProducts(self, documents):
        response = self.repository.insert_many(documents)
        _json_response = _json_convert(response.inserted_ids)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": [
                str(id["$oid"]) for id in _json_response
            ]
        }