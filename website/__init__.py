from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# APP DB Y UBICACION
db = SQLAlchemy()
DB_NAME = "database.db"


# Aplicacion Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'contraseña1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # Ubicacion de la DB
    db.init_app(app)  # Conectando la APP (Flask) a la DB



    # Llamando los blueprints al root
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('DATABASE CREADA!')
