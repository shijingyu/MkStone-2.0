from __future__ import unicode_literals

from django.db import models

#from mongoengine import *
from datetime import datetime
# Create your models here.

#
# class User(models.Model):
#     user = models.CharField(max_length=12)
#     password = models.CharField(max_length=16)
#     email = models.EmailField(max_length=30)
#     #qq = models.IntegerField()
#     regtime = models.DateTimeField(auto_now_add=True, blank=True)

class Res(models.Model):
    resname = models.CharField(max_length=60)
    http = models.CharField(max_length=128)
    resclass = models.CharField(max_length=16)
    uptime = models.DateTimeField(auto_now_add=True, blank=True)
    price = models.IntegerField()
    prow = models.IntegerField()
    rpassword = models.CharField(max_length=6)
    rpic = models.CharField(max_length=60)


class Article(models.Model):
    aname = models.CharField(max_length=60)
    aclass = models.CharField(max_length=16)
    auptime = models.DateTimeField(auto_now_add=True, blank=True)
    stars = models.IntegerField(default=0)
    author = models.CharField(max_length=12)
    apic = models.CharField(max_length=60)
    acontect = models.TextField(max_length=10000)
    amasonry = models.CharField(max_length=60)
    watch = models.IntegerField(default=1437)


class Qa(models.Model):
    quser = models.CharField(max_length=12)
    quesstion = models.CharField(max_length=64)
    qtime = models.DateTimeField(auto_now_add=True, blank=True)
    answer = models.CharField(max_length=100)
