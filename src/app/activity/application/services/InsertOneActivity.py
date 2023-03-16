from src.app.activity.infraestructure.DataBaseAdapter import ActivityRepository
from bson.json_util import _json_convert

class InsertOneActivity:
    def __init__(self):
        self.repository = ActivityRepository()

    def insertOneActivity(self, activity):
        response = self.repository.insert_one(activity)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": _json_convert(response.inserted_id)["$oid"]
        }