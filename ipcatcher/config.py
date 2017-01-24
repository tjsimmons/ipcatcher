DEBUG = False
SQLALCHEMY_DATABASE_URI = 'sqlite:////data/ipcatcher.db'

try:
    from local_config import *
except:
    pass
