from src.app.pond.domain.PondBSON import PondBSON
from src.app.pond.infraestructure.DataBaseAdapter import PondRepository
from bson import ObjectId
class UpdateOnePond:
    def __init__(self):
        self.repository = PondRepository()

    def update_pond_by_id(self, id, setPayload):
        response = self.repository.update_one({ "_id": ObjectId(id) }, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }
    def update_pond_by(self, filter, setPayload):
        response = self.repository.update_one(filter, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }