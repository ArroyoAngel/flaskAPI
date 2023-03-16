from src.app.auth.infraestructure.DataBaseAdapter import AccountRepository

class GetAccount:
    def __init__(self):
        self.repository = AccountRepository()

    def get_by(self, filter):
        self.repository.find(filter)

    def find_one(self, filter):
        self.repository.find_one(filter)