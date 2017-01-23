DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqllite://dev.db'

try:
    from local_config import *
except:
    pass
