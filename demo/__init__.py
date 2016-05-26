# -*- coding: utf-8 -*-
from flask import Flask

from .ext import cache
from .views import bp


def create_app(config=None):
    app = Flask(__name__)
    if config is None:
        config = 'config'
    app.config.from_object(config)

    cache.init_app(app)

    app.register_blueprint(bp)

    return app
