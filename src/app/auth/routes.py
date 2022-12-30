from flask import request, Blueprint, jsonify
from bson.json_util import _json_convert
from app.db import mongo

accounts = Blueprint('accounts', __name__, url_prefix='/accounts')
@accounts.route('/create', methods=['POST'])
def create_user():
    password = request.json["password"]
    email = request.json["email"]

    response = mongo.db.accounts.find({ "email": email })
    response = _json_convert(response)
    if len(response) > 0:
        return {
            "status": 500,
            "message": "El correo ya ha sido registrado."
        }

    if password and email:
        inserted = mongo.db.accounts.insert_one({ "email": email,"password": password})
        id = _json_convert(inserted.inserted_id)["$oid"]
        return {
            "status": 200,
            "id": id,
            "message": "Cuenta creada exitosamente",
            "payload": {"id": id,"email": email,"password": password}
        }
    else:
        return { 
            "status": 500,
            "message": "La información ingresada no es válida" 
        }

@accounts.route('/login', methods=['PUT'])
def login():
    email = request.json["email"]
    response = mongo.db.accounts.find({ "email": email })
    response = _json_convert(response)
    print(request.json["email"])
    if len(response)>0:
        mongo.db.accounts.update_one({
            "email": email
        }, {
            "$set": {
                "password": "ACTUALIZADO",
                "auth": "ACTUALIADO"
            }
        })
        return { "message": "UPDATED" }
    return { "message": "UNFOUNDED" }