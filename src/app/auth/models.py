class Account():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @staticmethod
    def find():
        pass

    def filter():
        pass
    
    def delete():
        pass

class AccountModel():
    def __init__(self, user_data):
        self.id = user_data.username
        self.password = user_data.password
    
    @staticmethod
    def login(user_id):
        pass

    def logut():
        pass

    def edit():
        pass