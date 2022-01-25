# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.auth_user_id import AuthUserId
from .api.protect import Protect


routes = [
    dict(resource=AuthUserId, urls=['/auth/<user_id>'], endpoint='auth_user_id'),
    dict(resource=Protect, urls=['/protect'], endpoint='protect'),
]