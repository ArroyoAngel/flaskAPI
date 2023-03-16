from src.app.auth.infraestructure.DataBaseAdapter import AccountRepository

class FindOneAccount:
    def __init__(self):
        self.repository = AccountRepository()

    def find_one_account(self, filter):
        response = self.repository.find_one(filter)
        return response
