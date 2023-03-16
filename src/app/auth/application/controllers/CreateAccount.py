from flask import Blueprint, request, jsonify, current_app
from src.app.auth.application.services.GetAccount import GetAccount
from src.app.auth.application.services.InsertOneAccount import InsertOneAccount
from werkzeug.security import generate_password_hash, check_password_hash

class CreateAccount:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/register', methods=['POST'], view_func=self.create_account)
    
    def create_account(self):
        with current_app.app_context():
            create_service = InsertOneAccount()
            get_service = GetAccount()
            
            # Obtiene los datos del usuario del cuerpo de la solicitud
            name = request.json['name']
            username = request.json['username']
            password = request.json['password']
            
            # Verifica si el correo electrónico ya está registrado
            if get_service.find_one({'username': username}):
                return jsonify({'error': 'Username already registered'})
            
            # Cifra la contraseña y guarda los datos del usuario en la base de datos
            hashed_password = generate_password_hash(password, method='sha256')
            user_id = create_service.insertOneAccount({'name': name, 'username': username, 'password': hashed_password})
            
            # Devuelve la respuesta con el ID del usuario registrado
        return jsonify({'user_id': str(user_id)})