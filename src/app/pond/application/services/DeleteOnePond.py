from src.app.pond.infraestructure.DataBaseAdapter import PondRepository
from bson import ObjectId

class DeleteOnePond:
    def __init__(self):
        self.repository = PondRepository()

    def delete_pond_by_id(self, item):
        response = self.repository.delete_one({"_id": ObjectId(item)})
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
        }

    def delete_pond_by(self, payload):
        response = self.repository.delete_one(payload)
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
        }