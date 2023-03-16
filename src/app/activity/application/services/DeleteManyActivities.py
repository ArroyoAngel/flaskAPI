from src.app.activity.infraestructure.DataBaseAdapter import ActivityRepository

class DeleteManyActivity:
    def __init__(self):
        self.repository = ActivityRepository()

    def delete_activities_by(self, payload):
        response = self.repository.delete_many(payload)
        return {
            "acknowledged": response.acknowledged,
            "deleted_count": response.deleted_count,
            "raw_result": response.raw_result
        }