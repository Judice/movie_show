# _*_ coding: utf-8 _*_
from wtforms import validators
from .. import db


class Movie(db.Document):
    name = db.StringField(required=True)
    year = db.IntField()
    month = db.IntField()
    day = db.IntField()
    img_url = db.StringField()
    download_links = db.ListField()
    date = db.IntField()
