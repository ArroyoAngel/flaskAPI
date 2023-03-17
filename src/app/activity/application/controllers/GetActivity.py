from src.app.activity.application.services.GetActivity import GetActivity as GetActivityService
from src.app.auth.application.controllers._authentication import operator_required
from flask import Blueprint, request

class GetActivity:
    def __init__(self, controller: Blueprint):
        self.service = GetActivityService()
        controller.add_url_rule('/', methods=['GET'], view_func=self.get_activities)
        controller.add_url_rule('/id=<string:id>', methods=['GET'], view_func=self.get_activity_by_id)
        controller.add_url_rule('/<string:key>=<string:value>', methods=['GET'], view_func=self.get_activities_by)

    @operator_required
    def get_activities(self, current_user):
        response = self.service.getActivities(request.json if request.data else None)
        return {
            "status": 200,
            "payload": response
        }
    
    @operator_required
    def get_activities_by(self, current_user, key=None, value=None, ):
        response = self.service.filterActivities(key, value)
        return {
            "status": 200,
            "payload": response
        }
    
    @operator_required
    def get_activity_by_id(self, current_user, id=None):
        response = self.service.getById(id)
        return {
            "status": 200,
            "payload": response
        }