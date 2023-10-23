from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
DB_NAME = "database.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'CHANHE LATER'
  app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:23516319@LAPTOP-DOQVNQFN/SQLserverapi?driver=ODBC+Driver+17+for+SQL+Server'
  db.init_app(app)

  ma.init_app(app)

  # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  # db.init_app(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix = '/')
  app.register_blueprint(auth, url_prefix = '/')

  from .models import TEST

  with app.app_context():
        db.create_all()

  # create_database(app)

  return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!') 