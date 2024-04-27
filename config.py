class Config:
    DEBUG = False
    TESTING = False
    # Add other configuration settings here

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    # Add more configurations as needed
}
# config/config.py

class Config:
    # MongoDB database URI
    MONGODB_URI = "mongodb://localhost:27017/mydatabase"

    # API keys or other sensitive information
    API_KEY = "your_api_key_here"
