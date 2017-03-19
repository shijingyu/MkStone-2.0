from __future__ import unicode_literals

from django.db import models

from mongoengine import *
from datetime import datetime
# Create your models here.

connect('MkStone')
class User(Document):
    user = StringField(max_length=12, required=True)
    password = StringField(max_length=16, required=True)
    email = EmailField(max_length=30, required=True)
    qq = IntField(max_length=12, required=True)
    token = StringField(max_length=128, required=True)
    is_active = IntField(default=0, required=True)
    regtime = DateTimeField(default=datetime.now(), required=True)

class Res(Document):
    resname = StringField(max_length=60, required=True)
    http = StringField(max_length=128, required=True)
    resclass = StringField(max_length=16, required=True)
    uptime = DateTimeField(default=datetime.now(), required=True)
    price = IntField(max_length=5, required=True)
    prow = IntField(max_length=10, required=True)
    rpassword = StringField(max_length=6, required=True)
    rpic = StringField(max_length=60, required=True)


class Article(Document):
    aname = StringField(max_length=60, required=True)
    aclass = StringField(max_length=16, required=True)
    auptime = DateTimeField(default=datetime.now(), required=True)
    stars = IntField(default=0, max_length=10, required=True)
    author = StringField(max_length=12, required=True)
    apic = StringField(max_length=60, required=True)
    acontect = StringField(max_length=10000, required=True)
    amasonry = StringField(max_length=60, required=True)
    watch = IntField(default=1437, max_length=10, required=True)


class Qa(Document):
    quser = StringField(max_length=12, required=True)
    quesstion = StringField(max_length=64, required=True)
    qtime = DateTimeField(default=datetime.now(), required=True)
    answer = StringField(max_length=100, required=True)
