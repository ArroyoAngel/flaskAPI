from src.app.product.application.services.GetProduct import GetProduct as GetProductService
from src.app.auth.application.controllers._authentication import operator_required
from flask import Blueprint, request

class GetProduct:
    def __init__(self, controller: Blueprint):
        self.service = GetProductService()
        controller.add_url_rule('/', methods=['GET'], view_func=self.get_products)
        controller.add_url_rule('/id=<string:id>', methods=['GET'], view_func=self.get_product_by_id)
        controller.add_url_rule('/<string:key>=<string:value>', methods=['GET'], view_func=self.get_products_by)

    @operator_required
    def get_products(self, current_product):
        response = self.service.getProducts(request.json if request.data else None)
        return {
            "status": 200,
            "payload": response
        }
    
    @operator_required
    def get_products_by(self, current_product, key=None, value=None, ):
        response = self.service.filterProducts(key, value)
        return {
            "status": 200,
            "payload": response
        }
    
    @operator_required
    def get_product_by_id(self, current_product, id=None):
        response = self.service.getById(id)
        return {
            "status": 200,
            "payload": response
        }