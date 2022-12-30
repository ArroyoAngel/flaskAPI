from flask import request, Blueprint
from .models import Users, User
from bson.objectid import ObjectId

_users_ = Users()
users = Blueprint('users', __name__, url_prefix='/users')
@users.route('/create', methods=['POST'])
def create():
    response = _users_.add(request.json)
    return response

@users.route('/get', methods=['POST'])
def get():
    _users_.get()
    print(_users_.data)
    return {
        "name": "NEVER"
    }

@users.route('/update/<id>', methods=['PUT'])
def update(id):
    payload = request.json
    user = User(_users_.find(id))
    objInstance = ObjectId(id)
    resolve = _users_.update({"_id": objInstance}, payload)
    return {
        "message": resolve
    }


@users.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    user = User(_users_.find(id))
    objInstance = ObjectId(id)
    resolve = _users_.delete({ "_id": objInstance })
    return resolve

@users.route('/upload', methods=['POST'])
def upload():
    pass