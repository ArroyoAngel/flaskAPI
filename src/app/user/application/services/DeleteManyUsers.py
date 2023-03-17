from src.app.user.infraestructure.DataBaseAdapter import UserRepository

class DeleteManyUser:
    def __init__(self):
        self.repository = UserRepository()

    def delete_users_by(self, payload):
        response = self.repository.delete_many(payload)
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
            "raw_result": response.raw_result
        }