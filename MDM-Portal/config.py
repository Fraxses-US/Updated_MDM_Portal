import os
from flask_appbuilder.security.manager import (
    AUTH_OID,
    AUTH_REMOTE_USER,
    AUTH_DB,
    AUTH_LDAP,
    AUTH_OAUTH,
)

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "\2\1thisismyscretkey\1\2\e\y\y\h"
SQLALCHEMY_DATABASE_URI = CLUTCH_PBM_URI = 'postgresql+psycopg2://{database_user}:{database_password}@{database_host}:{database_port}/{database_db}?options=-csearch_path%3Dclutch'.format(
    database_user='clutch', database_password='Intenda#01', database_host='104.196.221.210', database_port='5432', database_db='clutch')

#SQLALCHEMY_DATABASE_URI = CLUTCH_PBM_URI = 'postgresql+psycopg2://{database_user}:{database_password}@{database_host}:{database_port}/{database_db}?options=-csearch_path%3Dclutch'.format(database_user='clutch', database_password='Intenda#01', database_host='fraxses-pgr-svc-headless', database_port='5432', database_db='clutch')

SQLALCHEMY_BINDS = {
    'app':SQLALCHEMY_DATABASE_URI,
}

CSRF_ENABLED = True

APP_NAME = "Clutch"

AUTH_TYPE = AUTH_DB

UPLOAD_FOLDER = basedir + "/app/static/uploads/"

IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

IMG_UPLOAD_URL = "/static/uploads/"

FILE_ALLOWED_EXTENSIONS = ("txt", "pdf", "jpeg", "jpg", "gif", "png", "img")



