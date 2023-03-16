from src.app.activity.domain.ActivityBSON import ActivityBSON
from src.app.activity.infraestructure.DataBaseAdapter import ActivityRepository
from bson.json_util import _json_convert
from bson import ObjectId

class GetActivity:
    def __init__(self):
        self.repository = ActivityRepository()

    def getActivities(self, filter={}) -> list[ActivityBSON]:
        response = _json_convert(self.repository.find(filter))
        result = []
        for activity in response:
            result.append(ActivityBSON(activity).toDict())
        return result
    
    def getById(self, id) -> list[ActivityBSON]:
        response = _json_convert(self.repository.find({
            "_id": ObjectId(id)
        }))
        result = ActivityBSON(response[0]).toDict()
        return result
    
    def filterActivities(self, key, value) -> list[ActivityBSON]:
        filter = {}
        filter[key] = value
        response = _json_convert(self.repository.find(filter))
        result = []
        for activity in response:
            result.append(ActivityBSON(activity).toDict())
        
        return result
            