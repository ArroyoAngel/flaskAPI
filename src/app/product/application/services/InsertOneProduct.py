from src.app.product.infraestructure.DataBaseAdapter import ProductRepository
from bson.json_util import _json_convert

class InsertOneProduct:
    def __init__(self):
        self.repository = ProductRepository()

    def insertOneProduct(self, product):
        response = self.repository.insert_one(product)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": _json_convert(response.inserted_id)["$oid"]
        }