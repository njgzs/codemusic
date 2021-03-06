from flask import Flask,render_template
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_admin import Admin
import pymysql
pymysql.install_as_MySQLdb()




moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin()
login_manager.session_protection = 'base'
# login_manager.login_view = 'auth.login'
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    admin.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # from .admin import admin as adminManage_blueprint
    # app.register_blueprint(adminManage_blueprint)
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint,url_prefix='/auth')
    
    return app
    
     