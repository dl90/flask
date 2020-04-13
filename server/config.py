class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///db/database.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "maQ97z2uMNyWthgvrpKd36DfW4pbCkzFsdEJ6P54tq5wkzdNE2SA2JzJU7AjD3aotiU4go8p9usLFssa852GEd3n3UbpwVVUT4csDjEdSrFZnGXk68pEChHgVA5cmmuB"

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True