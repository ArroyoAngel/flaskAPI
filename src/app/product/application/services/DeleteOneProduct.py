from src.app.product.infraestructure.DataBaseAdapter import ProductRepository
from bson import ObjectId

class DeleteOneProduct:
    def __init__(self):
        self.repository = ProductRepository()

    def delete_product_by_id(self, item):
        response = self.repository.delete_one({"_id": ObjectId(item)})
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
        }

    def delete_product_by(self, payload):
        response = self.repository.delete_one(payload)
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
        }