from src.app.product.application.services.DeleteOneProduct import DeleteOneProduct
from src.app.product.application.services.DeleteManyProducts import DeleteManyProduct
from src.app.auth.application.controllers._authentication import administrator_required
from flask import Blueprint, request

class DeleteProduct:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['DELETE'], view_func=self.delete_one)
        controller.add_url_rule('/many', methods=['DELETE'], view_func=self.delete_many)

    @administrator_required
    def delete_one(self, current_product):
        service = DeleteOneProduct()
        if "id" in request.json:
            response = service.delete_product_by_id(request.json["id"])
        else:
            response = service.delete_product_by(request.json)
        return {
            "status": 200,
            "message": 'Usuario eliminado!',
            "payload": response
        }

    @administrator_required
    def delete_many(self, current_product):
        service = DeleteManyProduct()
        response = service.delete_products_by(request.json)
        return {
            "status": 200,
            "message": 'Usuarioes eliminados!',
            "payload": response
        }
