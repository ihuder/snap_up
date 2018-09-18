import os

from peewee import SqliteDatabase

BATH_PATH = os.path.dirname(os.path.abspath(__file__))
# db config
DB_TYPE = "sqlite"
DB_NAME = "inside.db"
DB_PATH = os.path.join(BATH_PATH, DB_NAME)
DB = SqliteDatabase(DB_PATH)
TEMPLATE_PATH = os.path.join(BATH_PATH, "template")
STATIC_PATH = os.path.join(BATH_PATH, "static")

SECRET_KEY = '9h4aovt1sd)-ycnjvp_zob$%@3gj6#4%w)-e#25eetr*6+@3l%'

DEBUG = True

LOGIN_URL = "/user/login"
