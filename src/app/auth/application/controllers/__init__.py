from flask import Blueprint , current_app
from src.app.auth.application.controllers.CreateAccount import CreateAccount
from src.app.auth.application.controllers.LoginAccount import LoginAccount

auth_controller = Blueprint('auth_controller', __name__, url_prefix='/auth')
CreateAccount(auth_controller)
LoginAccount(auth_controller)
