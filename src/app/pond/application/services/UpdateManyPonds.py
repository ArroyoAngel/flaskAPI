from src.app.pond.infraestructure.DataBaseAdapter import PondRepository

class UpdateManyPond:
    def __init__(self):
        self.repository = PondRepository()

    def update_pond_by(self, filter, setPayload):
        response = self.repository.update_many(filter, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }