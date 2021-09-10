# -*- coding: utf-8 -*- 
# date: 21-9-6 下午2:34
from flask import Blueprint

from app.models import Permission

main = Blueprint('main', __name__)


@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)


from . import views, errors
