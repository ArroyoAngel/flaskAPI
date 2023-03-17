from src.app.product.infraestructure.DataBaseAdapter import ProductRepository
from bson import ObjectId
class UpdateOneProduct:
    def __init__(self):
        self.repository = ProductRepository()

    def update_product_by_id(self, id, setPayload):
        response = self.repository.update_one({ "_id": ObjectId(id) }, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }
    def update_product_by(self, filter, setPayload):
        response = self.repository.update_one(filter, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }