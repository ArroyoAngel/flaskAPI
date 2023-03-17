from flask import Blueprint
from src.app.user.application.controllers.CreateUser import CreateUser
from src.app.user.application.controllers.GetUser import GetUser
from src.app.user.application.controllers.DeleteUser import DeleteUser
from src.app.user.application.controllers.UpdateUser import UpdateUser

user_controller = Blueprint('user_controller', __name__, url_prefix='/user')
CreateUser(user_controller)
GetUser(user_controller)
DeleteUser(user_controller)
UpdateUser(user_controller)