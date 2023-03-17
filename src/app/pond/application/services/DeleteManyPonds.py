from src.app.pond.infraestructure.DataBaseAdapter import PondRepository

class DeleteManyPond:
    def __init__(self):
        self.repository = PondRepository()

    def delete_ponds_by(self, payload):
        response = self.repository.delete_many(payload)
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
            "raw_result": response.raw_result
        }