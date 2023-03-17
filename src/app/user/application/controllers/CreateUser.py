from src.app.user.application.services.InsertOneUser import InsertOneUser
from src.app.user.application.services.InsertManyUsers import InsertManyUsers
from src.app.auth.application.controllers._authentication import administrator_required
from src.app.user.domain.User import User
from flask import Blueprint, request

class CreateUser:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['POST'], view_func=self.create_user)
        controller.add_url_rule('/many', methods=['POST'], view_func=self.create_user)
    
    @administrator_required
    def create_user(self, current_user):
        if isinstance(request.json, dict):
            return self.create_one_user()
        elif isinstance(request.json, list):
            return self.create_many_users()

    def create_one_user(self):
        payload = request.json
        service = InsertOneUser()
        user = User(payload).toDict()
        response = service.insertOneUser(user)
        return {
            "status": 200,
            "message": 'Usuario creado!',
            "payload": response
        }

    def create_many_users(self):
        payload = request.json
        service = InsertManyUsers()
        documents = []
        for user in payload:
            documents.append(User(user).toDict())

        response = service.insertManyUsers(documents)
        return {
            "status": 200,
            "message": 'Usuario creado!',
            "payload": response
        }
        
    
