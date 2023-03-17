from src.app.pond.application.services.InsertOnePond import InsertOnePond
from src.app.pond.application.services.InsertManyPonds import InsertManyPonds
from src.app.auth.application.controllers._authentication import administrator_required
from src.app.pond.domain.Pond import Pond
from flask import Blueprint, request

class CreatePond:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['POST'], view_func=self.create_pond)
        controller.add_url_rule('/many', methods=['POST'], view_func=self.create_pond)
    
    @administrator_required
    def create_pond(self, current_pond):
        if isinstance(request.json, dict):
            return self.create_one_pond()
        elif isinstance(request.json, list):
            return self.create_many_ponds()

    def create_one_pond(self):
        payload = request.json
        service = InsertOnePond()
        pond = Pond(payload).toDict()
        response = service.insertOnePond(pond)
        return {
            "status": 200,
            "message": 'Usuario creado!',
            "payload": response
        }

    def create_many_ponds(self):
        payload = request.json
        service = InsertManyPonds()
        documents = []
        for pond in payload:
            documents.append(Pond(pond).toDict())

        response = service.insertManyPonds(documents)
        return {
            "status": 200,
            "message": 'Usuario creado!',
            "payload": response
        }
        
    
