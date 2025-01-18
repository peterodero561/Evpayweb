'''Class for the database instance to be used'''

class Config:
    SECRET_KEY = 'peterdev1234'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://peterdev:Peter0dero!@localhost/evpay_db'

class TestingConfig:
    SECRET_KEY = 'peterdev1234'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://peterdev:Peter0dero!@localhost/evpay_test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

config = {
    'testing': TestingConfig,
    'config': Config
}