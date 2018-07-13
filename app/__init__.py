# app/__init.py__
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_admin import Admin

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass # Heroku does not use .env

db = SQLAlchemy()
ma = Marshmallow()
admin = Admin(name='admin', template_mode='bootstrap3')


def create_app() -> Flask:
    ''' Return a Flask application '''
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.main.controllers import main
    app.register_blueprint(main)

    db.init_app(app)
    ma.init_app(app)
    admin.init_app(app)

    return app
