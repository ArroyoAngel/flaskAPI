from src.app.activity.application.services.UpdateOneActivity import UpdateOneActivity
from src.app.activity.application.services.UpdateManyActivities import UpdateManyActivity
from src.app.auth.application.controllers._authentication import token_required
from flask import Blueprint, request

class UpdateActivity:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['PUT'], view_func=self.update_one)
        controller.add_url_rule('/many', methods=['PUT'], view_func=self.update_many)

    @token_required
    def update_one(self, current_user):
        service = UpdateOneActivity()
        filter = request.json["filter"]
        payload = request.json["payload"]
        if "id" in filter:
            response = service.update_activity_by_id(filter["id"], payload)
        else:
            response = service.update_activity_by(filter, payload)
        return response
    
    @token_required
    def update_many(self, current_user):
        service = UpdateManyActivity()
        filter = request.json["filter"]
        payload = request.json["payload"]
        response = service.update_activity_by(filter, payload)
        return response