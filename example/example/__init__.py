# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

from flask_jwt_extended import JWTManager

import v1


def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    app.config["JWT_SECRET_KEY"] = "mysecret"
    JWTManager(app)
    return app

if __name__ == '__main__':
    create_app().run(debug=True)
