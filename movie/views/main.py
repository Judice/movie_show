# _*_ coding: utf-8 _*_
from flask import render_template
from . import main_blueprint
from ..models.movie import Movie


@main_blueprint.route('/')
def index():
    movies = Movie.objects
    return render_template('index.html', movies=movies)
