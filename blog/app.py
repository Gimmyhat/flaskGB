from json import load
from os import getenv, path

from flask import Flask

from .article.views import article
from .auth.views import auth
from .extension import db, login_manager
from .index.views import index
from .models import User
from .report.views import report
from .user.views import user

CONFIG_PATH = getenv("CONFIG_PATH", path.join("..\dev_config.json"))

VIEWS = [
    index,
    user,
    article,
    report,
    auth
]


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_file(CONFIG_PATH, load)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
