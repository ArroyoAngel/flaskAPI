from src.app.user.application.services.UpdateOneUser import UpdateOneUser
from src.app.user.application.services.UpdateManyUsers import UpdateManyUser
from src.app.auth.application.controllers._authentication import administrator_required
from flask import Blueprint, request

class UpdateUser:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['PUT'], view_func=self.update_one)
        controller.add_url_rule('/many', methods=['PUT'], view_func=self.update_many)

    @administrator_required
    def update_one(self, current_user):
        service = UpdateOneUser()
        filter = request.json["filter"]
        payload = request.json["payload"]
        if "id" in filter:
            response = service.update_user_by_id(filter["id"], payload)
        else:
            response = service.update_user_by(filter, payload)
        return {
            "status": 200,
            "message": 'Usuario actualizado!',
            "payload": response
        }
    
    @administrator_required
    def update_many(self, current_user):
        service = UpdateManyUser()
        filter = request.json["filter"]
        payload = request.json["payload"]
        response = service.update_user_by(filter, payload)
        return {
            "status": 200,
            "message": 'Usuarios actualizados!',
            "payload": response
        }