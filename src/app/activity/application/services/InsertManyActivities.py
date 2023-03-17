from src.app.activity.domain.Activity import Activity
from src.app.activity.infraestructure.DataBaseAdapter import ActivityRepository
from bson.json_util import _json_convert

class InsertManyActivities:
    def __init__(self):
        self.repository = ActivityRepository()

    def insertManyActivities(self, payload):
        documents = []
        for document in payload:
            documents.append(Activity(document).toBson())
        response = self.repository.insert_many(documents)
        _json_response = _json_convert(response.inserted_ids)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": [
                str(id["$oid"]) for id in _json_response
            ]
        }