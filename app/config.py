DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////dev.db'

try:
    from local_config import *
except:
    pass
