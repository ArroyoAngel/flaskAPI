from src.app.activity.infraestructure.DataBaseAdapter import ActivityRepository

class UpdateManyActivity:
    def __init__(self):
        self.repository = ActivityRepository()

    def update_activity_by(self, filter, setPayload):
        response = self.repository.update_many(filter, { "$set": setPayload})
        return {
            "acknowledged": response.acknowledged,
            "matched_count": response.matched_count,
            "modified_count": response.modified_count,
            "upserted_id": response.upserted_id,
        }