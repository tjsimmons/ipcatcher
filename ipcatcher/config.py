DEBUG = False
DB_NAME = 'dev'
DB_USER = 'postgres'
DB_PASS = 'postgres'
DB_SERVICE = 'postgres'
DB_PORT = '5342'
SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
)

try:
    from local_config import *
except:
    pass
