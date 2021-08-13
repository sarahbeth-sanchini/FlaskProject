# app/__init__.py (ROOT PACKAGE)
# PYTHON CODE FOR SECTION : 11 LECTURE : 42 (flask-bcrypt and flask-login)


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
# migrate = Migrate()
bootstrap = Bootstrap()
#login_manager = LoginManager()
#bcrypt = Bcrypt()

##NOTES:
#because we are using scalable code, we need a python fuction to create an instance.
#we will not create a global flask instance because our structure is now modular

#Can be passed either dev, test or prod - this is an app factory
def create_app(config_type):

    app = Flask(__name__)

    #load the absolute path to the configuration file
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    #INIT section - pass the flask instance to the other instances to bind them
    db.init_app(app)
    # migrate.init_app(app, db)
    bootstrap.init_app(app)
    #login_manager.init_app(app)
    #bcrypt.init_app(app)

    #Import and Register Blueprints
    from app.catalog import main #location of file in app->category (NOT the flask instance)
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app
