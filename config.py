import os

class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass 


class DevConfig(Config):
    DEBUG = True


config_options = {
'development': DevConfig,
'production': ProdConfig,
'test': TestConfig
}