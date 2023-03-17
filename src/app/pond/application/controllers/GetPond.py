from src.app.pond.application.services.GetPond import GetPond as GetPondService
from src.app.auth.application.controllers._authentication import operator_required
from flask import Blueprint, request

class GetPond:
    def __init__(self, controller: Blueprint):
        self.service = GetPondService()
        controller.add_url_rule('/', methods=['GET'], view_func=self.get_ponds)
        controller.add_url_rule('/id=<string:id>', methods=['GET'], view_func=self.get_pond_by_id)
        controller.add_url_rule('/<string:key>=<string:value>', methods=['GET'], view_func=self.get_ponds_by)

    @operator_required
    def get_ponds(self, current_pond):
        response = self.service.getPonds(request.json if request.data else None)
        return {
            "status": 200,
            "payload": response
        }
    
    @operator_required
    def get_ponds_by(self, current_pond, key=None, value=None, ):
        response = self.service.filterPonds(key, value)
        return {
            "status": 200,
            "payload": response
        }
    
    @operator_required
    def get_pond_by_id(self, current_pond, id=None):
        response = self.service.getById(id)
        return {
            "status": 200,
            "payload": response
        }