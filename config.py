import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sharon-maswai:qwerty@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    pass


class DevConfig(Config):
   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}