# -*- coding: utf-8 -*- 
# date: 21-9-6 下午4:19
from flask import Blueprint


auth = Blueprint('auth', __name__)


from . import views
