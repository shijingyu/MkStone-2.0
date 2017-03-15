from __future__ import unicode_literals

from django.db import models

from mongoengine import *
from datetime import datetime
# Create your models here.

connect('lol')
class Categories(Document):
    name = StringField(max_length=30, required=True)
    artnum = IntField(default=0, required=True)
    date = DateTimeField(default=datetime.now(), required=True)
