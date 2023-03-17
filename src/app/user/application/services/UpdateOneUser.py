from src.app.user.domain.UserBSON import UserBSON
from src.app.user.infraestructure.DataBaseAdapter import UserRepository
from bson import ObjectId
class UpdateOneUser:
    def __init__(self):
        self.repository = UserRepository()

    def update_user_by_id(self, id, setPayload):
        response = self.repository.update_one({ "_id": ObjectId(id) }, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }
    def update_user_by(self, filter, setPayload):
        response = self.repository.update_one(filter, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }