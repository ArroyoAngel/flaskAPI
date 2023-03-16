from flask import Blueprint
from src.app.activity.application.controllers.CreateActivity import CreateActivity
from src.app.activity.application.controllers.GetActivity import GetActivity
from src.app.activity.application.controllers.DeleteActivity import DeleteActivity
from src.app.activity.application.controllers.UpdateActivity import UpdateActivity

activity_controller = Blueprint('activity_controller', __name__, url_prefix='/activity')
CreateActivity(activity_controller)
GetActivity(activity_controller)
DeleteActivity(activity_controller)
UpdateActivity(activity_controller)