from src.app.activity.application.services.InsertOneActivity import InsertOneActivity
from src.app.activity.application.services.InsertManyActivities import InsertManyActivities
from src.app.activity.domain.Activity import Activity
from flask import Blueprint, request

class CreateActivity:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['POST'], view_func=self.create_activity)
        controller.add_url_rule('/many', methods=['POST'], view_func=self.create_activity)
    
    def create_activity(self):
        if isinstance(request.json, dict):
            return self.create_one_activity()
        elif isinstance(request.json, list):
            return self.create_many_activities()

    def create_one_activity(self):
        payload = request.json
        service = InsertOneActivity()
        activity = Activity(payload).toDict()
        response = service.insertOneActivity(activity)
        return {
            "status": 200,
            "message": 'Actividad creada!',
            "payload": response
        }

    def create_many_activities(self):
        payload = request.json
        service = InsertManyActivities()
        documents = []
        for activity in payload:
            documents.append(Activity(activity).toDict())

        response = service.insertManyActivities(documents)
        return {
            "status": 200,
            "message": 'Actividad creada!',
            "payload": response
        }
        
    
