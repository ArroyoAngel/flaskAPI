from src.app.user.application.services.GetUser import GetUser as GetUserService
from src.app.auth.application.controllers._authentication import operator_required
from flask import Blueprint, request

class GetUser:
    def __init__(self, controller: Blueprint):
        self.service = GetUserService()
        controller.add_url_rule('/', methods=['GET'], view_func=self.get_users)
        controller.add_url_rule('/id=<string:id>', methods=['GET'], view_func=self.get_user_by_id)
        controller.add_url_rule('/<string:key>=<string:value>', methods=['GET'], view_func=self.get_users_by)

    @operator_required
    def get_users(self, current_user):
        response = self.service.getUsers(request.json if request.data else None)
        return {
            "status": 200,
            "payload": response
        }
    
    @operator_required
    def get_users_by(self, current_user, key=None, value=None, ):
        response = self.service.filterUsers(key, value)
        return {
            "status": 200,
            "payload": response
        }
    
    @operator_required
    def get_user_by_id(self, current_user, id=None):
        response = self.service.getById(id)
        return {
            "status": 200,
            "payload": response
        }