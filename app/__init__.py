from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import Config
from flask_ckeditor import CKEditor
import babel


db = SQLAlchemy()
ckeditor = CKEditor()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.login_message_category = "info"

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.template_filter()
    def format_datetime(value, format='medium'):
        if format == 'full':
            format="EEEE, d MMMM y 'saat' HH:mm"
        elif format == 'medium':
            format="EE dd.MM.y HH:mm"
        return babel.dates.format_datetime(value, format)

    ckeditor.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.main.routes import main
    from app.admin.routes import admin
    from app.error.handlers import error

    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(error)

    @app.errorhandler(400)
    def unprocessable_entity(error):
        return render_template("/errors/400.html")

    @app.errorhandler(401)
    def unauthorized(error):
        return render_template("/errors/401.html")

    @app.errorhandler(403)
    def forbidden(error):
        return render_template("/errors/403.html")

    @app.errorhandler(404)
    def not_found(error):
        return render_template("/errors/404.html")

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("/errors/500.html")

    return app
