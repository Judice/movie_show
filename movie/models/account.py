# _*_ coding: utf-8 _*_
from .. import db


class Account(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True)

    meta = {"db_alias": "account"}
