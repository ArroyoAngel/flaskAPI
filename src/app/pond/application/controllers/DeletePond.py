from src.app.pond.application.services.DeleteOnePond import DeleteOnePond
from src.app.pond.application.services.DeleteManyPonds import DeleteManyPond
from src.app.auth.application.controllers._authentication import administrator_required
from flask import Blueprint, request

class DeletePond:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['DELETE'], view_func=self.delete_one)
        controller.add_url_rule('/many', methods=['DELETE'], view_func=self.delete_many)

    @administrator_required
    def delete_one(self, current_pond):
        service = DeleteOnePond()
        if "id" in request.json:
            response = service.delete_pond_by_id(request.json["id"])
        else:
            response = service.delete_pond_by(request.json)
        return {
            "status": 200,
            "message": 'Usuario eliminado!',
            "payload": response
        }

    @administrator_required
    def delete_many(self, current_pond):
        service = DeleteManyPond()
        response = service.delete_ponds_by(request.json)
        return {
            "status": 200,
            "message": 'Usuarioes eliminados!',
            "payload": response
        }
