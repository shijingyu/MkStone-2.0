#coding:utf-8
from django.shortcuts import render

from django.http import HttpResponse
from PythonMkStone.models import *
from django import forms


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def res(request):
    res = Res.objects.all()
    return render(request, 'res.html', {'res':res})
    return render(request, 'res.html')
def res2(request):
    return render(request, 'res2.html')

def addres(request):
    return render(request, 'addres.html')

def AddResForm(request):
    addresforms = Res()
    addresforms.resname = request.POST['resname']
    addresforms.resclass = request.POST['resclass']
    addresforms.http = request.POST['http']
    addresforms.price = request.POST['price']
    addresforms.uptime = request.POST['uptime']
    addresforms.prow = request.POST['prow']
    addresforms.rpassword = request.POST['rpassword']
    addresforms.rpic = request.POST['rpic']
    addresforms.save()
    string = '资源添加成功'
    return HttpResponse(string)
def ask(request):
    return render(request, 'ask.html')
def article(request):
    aall = Article.objects.all()
    return render(request, 'article.html', {'aall':aall})
def video(request):
    return render(request, 'video.html')
def login_register(request):
    return render(request, 'login_register.html')
    # username = request.POST['username']
    # password = request.POST['password']

def email(request):
    return render(request, 'sendemail.html')
def admin_index(request):
    return render(request, 'admin_index.html')



def addarticle(request):
    return render(request, 'addarticle.html')

def AddArticleForm(request):
    addarticleforms = Article()
    addarticleforms.aname = request.POST['title']
    addarticleforms.auptime = request.POST['upload']
    addarticleforms.author = request.POST['author']
    addarticleforms.aclass = request.POST['cat_id']
    addarticleforms.acontect = request.POST['content']
    addarticleforms.amasonry = request.POST['img1']
    addarticleforms.apic = request.POST['img2']
    addarticleforms.watch = request.POST['watch']
    addarticleforms.save()
    string = '文章添加成功'
    return HttpResponse(string)
def article_show(request):
    ashows = Article.objects.all()
    return render(request, 'article_show.html', {'ashows':ashows})
# def deletearticle(request):


def res_show(request):
    rshows = Res.objects.all()
    return render(request, 'res_show.html', {'rshows':rshows})

def admin_login(request):
    return render(request, 'admin-login.html')
# newuser = Article()
# newuser.aname = 'sd1'on) == del:

# newuser.aclass = 'china'
# newuser.stars = 112
# newuser.save()
# cate = Article.objects(aname="sd1")
# print cate.aname()
# cate = Article.objects().all()
# print cate[0]['aname']
# adata = Article.objects.all()
# acount = adata.count()
# print acount
# aall = Article.objects.all()
# acount = aall.count()
#
# i = 0
# while i < acount :
#     adata = aall[i]['id']
#     print adata
#     i += 1
