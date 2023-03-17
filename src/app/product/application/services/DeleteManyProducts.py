from src.app.product.infraestructure.DataBaseAdapter import ProductRepository

class DeleteManyProduct:
    def __init__(self):
        self.repository = ProductRepository()

    def delete_products_by(self, payload):
        response = self.repository.delete_many(payload)
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
            "raw_result": response.raw_result
        }