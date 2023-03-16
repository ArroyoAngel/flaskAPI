from src.app.auth.application.services.FindOneAccount import FindOneAccount
from flask import request, jsonify
from functools import wraps
import jwt

def administrator_required(f):
    @wraps(f)
    def decorated(instance, *args, **kwargs):
        service = FindOneAccount()
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]

        if not token:
            return jsonify({'message': 'Token no encontrado!'}), 401

        try:
            data = jwt.decode(token, 'my_secret_key', algorithms=['HS256'])
            current_user = service.find_one_account({'username': data['username']})
            if current_user['role'] != 'administrator':
                return jsonify({'message': 'No tienes los permisos necesarios!'}), 401
        except:
            return jsonify({'message': 'Token invalido!'}), 401

        return f(instance, current_user, *args, **kwargs)

    return decorated

def operator_required(f):
    @wraps(f)
    def decorated(instance, *args, **kwargs):
        service = FindOneAccount()
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]

        if not token:
            return jsonify({'message': 'Token no encontrado!'}), 401

        try:
            data = jwt.decode(token, 'my_secret_key', algorithms=['HS256'])
            current_user = service.find_one_account({'username': data['username']})
            if current_user['role'] != 'administrator' and current_user['role'] != 'operator' :
                return jsonify({'message': 'No tienes los permisos necesarios!'}), 401
        except:
            return jsonify({'message': 'Token invalido!'}), 401

        return f(instance, current_user, *args, **kwargs)

    return decorated