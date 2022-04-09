from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_ckeditor import CKEditor

db = SQLAlchemy()
ckeditor = CKEditor()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    ckeditor.init_app(app)

    db.init_app(app)

    from app.main.routes import main
    from app.admin.routes import admins
    from app.error.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(admins)
    app.register_blueprint(errors)

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
