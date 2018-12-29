#!flask/bin/python
from migrate.versioning import api
from config import Config
#from config import SQLALCHEMY_DATABASE_URI
#from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path

cfg = Config()

SQLALCHEMY_DATABASE_URI = cfg.SQLALCHEMY_DATABASE_URI
SQLALCHEMY_MIGRATE_REPO = cfg.SQLALCHEMY_MIGRATE_REPO

print(SQLALCHEMY_DATABASE_URI)
db.create_all()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
	api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
	api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
