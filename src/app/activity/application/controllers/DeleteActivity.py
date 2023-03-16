from src.app.activity.application.services.DeleteOneActivity import DeleteOneActivity
from src.app.activity.application.services.DeleteManyActivities import DeleteManyActivity
from src.app.auth.application.controllers._authentication import administrator_required
from flask import Blueprint, request

class DeleteActivity:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['DELETE'], view_func=self.delete_one)
        controller.add_url_rule('/many', methods=['DELETE'], view_func=self.delete_many)

    @administrator_required
    def delete_one(self, current_user):
        service = DeleteOneActivity()
        if "id" in request.json:
            response = service.delete_activity_by_id(request.json["id"])
        else:
            response = service.delete_activity_by(request.json)
        return {
            "status": 200,
            "message": 'Actividad eliminada!',
            "payload": response
        }

    @administrator_required
    def delete_many(self, current_user):
        service = DeleteManyActivity()
        response = service.delete_activities_by(request.json)
        return {
            "status": 200,
            "message": 'Actividades eliminadas!',
            "payload": response
        }
