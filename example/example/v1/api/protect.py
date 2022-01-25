# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from . import Resource
from .. import schemas


class Protect(Resource):

    @jwt_required()
    def get(self):
        print("Protect get")
        userid = get_jwt_identity()

        return userid, 200, None
