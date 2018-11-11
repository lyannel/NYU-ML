from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

SQL = Flask(__name__)
SQL.config.from_object(Config)
db = SQLAlchemy(SQL)
migrate = Migrate(SQL, db)

from SQL import routes,models