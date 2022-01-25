# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
from flask import jsonify
from flask_jwt_extended import create_access_token

from . import Resource
from .. import schemas


class AuthUserId(Resource):

    def get(self, user_id):
        print("auth get")
        atoken = create_access_token(identity=str(user_id))

        return jsonify(access_token=atoken)
