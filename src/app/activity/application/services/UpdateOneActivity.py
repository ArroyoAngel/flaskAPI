from src.app.activity.domain.ActivityBSON import ActivityBSON
from src.app.activity.infraestructure.DataBaseAdapter import ActivityRepository
from bson import ObjectId
class UpdateOneActivity:
    def __init__(self):
        self.repository = ActivityRepository()

    def update_activity_by_id(self, id, setPayload):
        response = self.repository.update_one({ "_id": ObjectId(id) }, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }
    def update_activity_by(self, filter, setPayload):
        response = self.repository.update_one(filter, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }