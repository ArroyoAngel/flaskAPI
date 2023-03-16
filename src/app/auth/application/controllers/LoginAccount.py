from flask import Blueprint, request, jsonify
from src.app.auth.application.services.FindOneAccount import FindOneAccount
import jwt
from werkzeug.security import check_password_hash
import datetime

class LoginAccount:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/login', methods=['POST'], view_func=self.login_account)

    def login_account(self):
        auth = request.authorization
        service = FindOneAccount()
        
        user = service.find_one_account({'username': auth.username})
        
        if user and check_password_hash(user['password'], auth.password):
            token = jwt.encode(
                {'username': user['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                'my_secret_key', 
                algorithm='HS256'
            )
            return {
                "status": 200,
                "message": 'Login completado!',
                "payload": jsonify({'token': token})
            }
        else:
            return {
                "status": 401,
                "message": 'La contrasena es incorrecta!',
                "payload": jsonify({'error': 'Authentication failed'})
            }
        

