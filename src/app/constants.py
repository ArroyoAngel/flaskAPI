####    MONGO DB CONSTANTS    ####
class COLLECTIONS:
    ACTIVITY = "activity"
    ACCOUNT = "account"
    USER = "user"
    PRODUCTS = "products"
    POND = "pond"

class DATABASE:
    URI = "mongodb://localhost:27017"
    NAME = "flaskapi"
    COLLECTIONS = COLLECTIONS()

