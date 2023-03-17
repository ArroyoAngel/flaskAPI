from src.app.user.infraestructure.DataBaseAdapter import UserRepository
from bson import ObjectId

class DeleteOneUser:
    def __init__(self):
        self.repository = UserRepository()

    def delete_user_by_id(self, item):
        response = self.repository.delete_one({"_id": ObjectId(item)})
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
        }

    def delete_user_by(self, payload):
        response = self.repository.delete_one(payload)
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
        }