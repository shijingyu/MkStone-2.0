#coding:utf-8
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from PythonMkStone.models import *
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages, auth
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext

from itsdangerous import URLSafeTimedSerializer as utsr
import base64
import re
from django.conf import settings as django_settings
# global a
# a = 3
class Token:
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodestring(security_key)
    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        return serializer.dumps(username, self.salt)
    def confirm_validate_token(self, token, expiration=3600):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)
    def remove_validate_token(self, token):
        serializer = utsr(self.security_key)
	    #print serializer.loads(token, salt=self.salt)
        return serializer.loads(token, salt=self.salt)

token_confirm = Token(django_settings.SECRET_KEY)    # 定义为全局变量


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def res(request):
    res = Res.objects.all()
    return render(request, 'res.html', {'res':res})

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
    return render(request, 'admin_login.html')

def admin_login_success(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = auth.authenticate(username=username, password=password)
    # if user is not None and username == u'我是石头哥哥':
    #
    #
    #
    #     return render(request, 'admin_index.html', {'a':a})
    # else:
    #     return render(request, 'message.html', {'messages':u'管理员账号密码错误'})

    return render(request, 'message.html', {'messages': u'管理员账号密码错误'})

def login(request):
    username = request.POST['username']
    password = request.POST['password']

   # user_1 = User.objects.filter(user__exact = a, password__exact = b)
    #if user_1:
       # request.session['user_user'] =user.user
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return render_to_response('login_success.html', RequestContext(request, {'username':username}))
        else:
            return render_to_response('token_error.html', RequestContext(request, {'username':username}))
    else:
        return render_to_response('login_error.html', RequestContext(request))
# else:
#     return render(request, 'login_error.html')

def login_error(request):
    return render(request, 'login_error.html')

def login_success(request):
    return render(request, 'login_success.html')

def logup(request):
    u = request.POST['username']
    userrow = User.objects.filter(username=u)[:1]
    if len(userrow)>0:
        return render(request, 'login_again.html')
    else:
        pppassword = request.POST['password']
        eeemail = request.POST['email']
        #adduser.qq =request.POST['qq']
        user = User.objects.create_user(u, eeemail, pppassword)
        user.is_active = False
        user.save()
        token = token_confirm.generate_validate_token(u)
        message = "\n".join([u'{0}, 欢迎加入MkStone'.format(u), u'请访问该链接，完成用户验证:',
                             '/'.join([django_settings.DOMAIN, 'activate', token])])
        send_mail(u'MkStone注册验证邮件', message, 'shijy675497282@163.com', [eeemail], fail_silently=False)
        return render(request, 'message.html', {'message': u"请登录到注册邮箱中验证用户，有效期为1个小时"})
       # return render(request, 'logup_success.html',{'user':u})


def logup_success(request):
    return render(request, 'logup_success.html')

def login_again(request):
    return render(request, 'login_again.html')

def usename(request):
    usenames = User.objects.all()
    return render(request, 'usename.html', {'usenames':usenames})

def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')

def my(request):
    mys = User.objects.all()
    return render(request, 'my.html', {'mys':mys})

def token_error(request):
    return render(request, 'token_error.html')

def active_user(requset, token):
    try:
        username = token_confirm.confirm_validate_token(token)
    except:
        username = token_confirm.remove_validate_token(token)
        users = User.objects.filter(username=username)
        #for user in users:
           # user.delete()
        return render(request, 'message.html', {
            'message': u'对不起，验证链接已经过期，请重新注册'})
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request, 'message.html', {'message': u"对不起，您所验证的用户不存在，请重新注册"})
    user.is_active = True
    user.save()
    message = u'验证成功，请进行登陆，享受MkStone'
    return render_to_response('message.html', {'message': message})
def help(request):
    return render(request, 'help.html')

def hand(request):
    return render(request, 'hand.html')