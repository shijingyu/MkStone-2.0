#coding:utf-8
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def res(request):
    return render(request, 'res.html')
def ask(request):
    return render(request, 'ask.html')
def article(request):
    return render(request, 'article.html')
def video(request):
    return render(request, 'video.html')
def login_register(request):
    return render(request, 'login_register.html')
def email(request):
    return render(request, 'sendemail.html')
def admin_index(request):
    return render(request, 'admin_index.html')


from PythonMkStone.models import Categories

cate = Categories(name='Linux')
cate.save()