from src.app.activity.domain.Activity import Activity
from src.app.activity.infraestructure.DataBaseAdapter import ActivityRepository
from bson import ObjectId

class GetActivity:
    def __init__(self):
        self.repository = ActivityRepository()

    def getActivities(self, filter={}):
        if filter !=None and "_id" in filter:
            filter = { "_id": ObjectId(filter["id"]) }
        response = list(self.repository.find(filter))
        result = []
        for activity in response:
            result.append(Activity(activity).toDict())
        return result
    
    def getById(self, id):
        response = list(self.repository.find({
            "_id": ObjectId(id)
        }))
        activity = response[0]
        result = Activity(activity).toDict()
        return result
    
    def filterActivities(self, key, value):
        filter = {}
        filter[key] = value
        response = list(self.repository.find(filter))
        result = []
        for activity in response:
            result.append(Activity(activity).toDict())
        
        return result
            