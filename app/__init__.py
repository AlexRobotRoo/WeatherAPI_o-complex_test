from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key'  # Уникальный секретный ключ
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app