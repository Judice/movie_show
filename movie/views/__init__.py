# _*_ coding: utf-8 _*_
from flask import Blueprint

main_blueprint = Blueprint('main', __name__)
auth_blueprint = Blueprint('auth', __name__)

from . import main, auth
