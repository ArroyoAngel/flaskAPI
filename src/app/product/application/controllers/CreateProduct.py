from src.app.product.application.services.InsertOneProduct import InsertOneProduct
from src.app.product.application.services.InsertManyProducts import InsertManyProducts
from src.app.auth.application.controllers._authentication import administrator_required
from src.app.product.domain.Product import Product
from flask import Blueprint, request

class CreateProduct:
    def __init__(self, controller: Blueprint):
        controller.add_url_rule('/', methods=['POST'], view_func=self.create_product)
        controller.add_url_rule('/many', methods=['POST'], view_func=self.create_product)
    
    @administrator_required
    def create_product(self, current_product):
        if isinstance(request.json, dict):
            return self.create_one_product()
        elif isinstance(request.json, list):
            return self.create_many_products()

    def create_one_product(self):
        payload = request.json
        service = InsertOneProduct()
        product = Product(payload).toDict()
        response = service.insertOneProduct(product)
        return {
            "status": 200,
            "message": 'Usuario creado!',
            "payload": response
        }

    def create_many_products(self):
        payload = request.json
        service = InsertManyProducts()
        documents = []
        for product in payload:
            documents.append(Product(product).toDict())

        response = service.insertManyProducts(documents)
        return {
            "status": 200,
            "message": 'Usuario creado!',
            "payload": response
        }
        
    
