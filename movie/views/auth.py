# _*_ coding: utf-8 _*_
from flask import render_template
from . import auth_blueprint


@auth_blueprint.route('/')
def index():
    return render_template('index.html')