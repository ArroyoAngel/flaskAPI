from flask import Blueprint
from src.app.product.application.controllers.CreateProduct import CreateProduct
from src.app.product.application.controllers.GetProduct import GetProduct
from src.app.product.application.controllers.DeleteProduct import DeleteProduct
from src.app.product.application.controllers.UpdateProduct import UpdateProduct

product_controller = Blueprint('product_controller', __name__, url_prefix='/product')
CreateProduct(product_controller)
GetProduct(product_controller)
DeleteProduct(product_controller)
UpdateProduct(product_controller)