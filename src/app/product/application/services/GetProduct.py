from src.app.product.domain.Product import Product
from src.app.product.infraestructure.DataBaseAdapter import ProductRepository
from bson import ObjectId

class GetProduct:
    def __init__(self):
        self.repository = ProductRepository()

    def getProducts(self, filter={}):
        if filter !=None and "_id" in filter:
            filter = { "_id": ObjectId(filter["id"]) }
        response = list(self.repository.find(filter))
        result = []
        for product in response:
            result.append(Product(product).toDict())
        return result
    
    def getById(self, id):
        response = list(self.repository.find({
            "_id": ObjectId(id)
        }))
        product = response[0]
        result = Product(product).toDict()
        return result
    
    def filterProducts(self, key, value):
        filter = {}
        filter[key] = value
        response = list(self.repository.find(filter))
        result = []
        for product in response:
            result.append(Product(product).toDict())
        
        return result
            