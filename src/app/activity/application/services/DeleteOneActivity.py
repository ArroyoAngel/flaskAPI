from src.app.activity.infraestructure.DataBaseAdapter import ActivityRepository
from bson import ObjectId

class DeleteOneActivity:
    def __init__(self):
        self.repository = ActivityRepository()

    def delete_activity_by_id(self, item):
        response = self.repository.delete_one({"_id": ObjectId(item)})
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
        }

    def delete_activity_by(self, payload):
        response = self.repository.delete_one(payload)
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
        }