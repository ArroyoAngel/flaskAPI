from flask import Blueprint
from src.app.pond.application.controllers.CreatePond import CreatePond
from src.app.pond.application.controllers.GetPond import GetPond
from src.app.pond.application.controllers.DeletePond import DeletePond
from src.app.pond.application.controllers.UpdatePond import UpdatePond

pond_controller = Blueprint('pond_controller', __name__, url_prefix='/pond')
CreatePond(pond_controller)
GetPond(pond_controller)
DeletePond(pond_controller)
UpdatePond(pond_controller)