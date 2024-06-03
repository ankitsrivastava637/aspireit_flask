class Config:
    SECRET_KEY = 'secret_key'
    MONGO_URI = 'mongodb://localhost:27017/aspireit_db'
    JWT_SECRET_KEY = 'jwt_secret_key'

class TestConfig(Config):
    TESTING = True
    MONGO_URI = 'mongodb://localhost:27017/aspireit_test_db'