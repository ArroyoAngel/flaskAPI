from src.app.product.infraestructure.DataBaseAdapter import ProductRepository

class UpdateManyProduct:
    def __init__(self):
        self.repository = ProductRepository()

    def update_product_by(self, filter, setPayload):
        response = self.repository.update_many(filter, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }