from flask_pymongo import ObjectId

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def from_dict(data):
        return User(username=data.get('username'), password=data.get('password'))

    def to_dict(self):
        return {'username': self.username, 'password': self.password}


