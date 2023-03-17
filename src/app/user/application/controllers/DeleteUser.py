from src.app.user.application.services.DeleteOneUser import DeleteOneUser
from src.app.user.application.services.DeleteManyUsers import DeleteManyUser
from src.app.auth.application.controllers._authentication import administrator_required
from flask import Blueprint, request

class DeleteUser:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['DELETE'], view_func=self.delete_one)
        controller.add_url_rule('/many', methods=['DELETE'], view_func=self.delete_many)

    @administrator_required
    def delete_one(self, current_user):
        service = DeleteOneUser()
        if "id" in request.json:
            response = service.delete_user_by_id(request.json["id"])
        else:
            response = service.delete_user_by(request.json)
        return {
            "status": 200,
            "message": 'Usuario eliminado!',
            "payload": response
        }

    @administrator_required
    def delete_many(self, current_user):
        service = DeleteManyUser()
        response = service.delete_users_by(request.json)
        return {
            "status": 200,
            "message": 'Usuarioes eliminados!',
            "payload": response
        }
