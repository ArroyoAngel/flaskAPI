from src.app.user.infraestructure.DataBaseAdapter import UserRepository

class UpdateManyUser:
    def __init__(self):
        self.repository = UserRepository()

    def update_user_by(self, filter, setPayload):
        response = self.repository.update_many(filter, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }