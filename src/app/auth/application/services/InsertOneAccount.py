from src.app.auth.infraestructure.DataBaseAdapter import AccountRepository
from bson.json_util import _json_convert
class InsertOneAccount:
    def __init__(self):
        self.repository = AccountRepository()

    def insertOneAccount(self, account):
        response = self.repository.insert_one(account)
        return {
            "acknowledged": response.acknowledged,
            "inserted_id": _json_convert(response.inserted_id)["$oid"]
        }