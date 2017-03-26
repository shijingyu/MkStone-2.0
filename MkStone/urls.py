"""MkStone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from PythonMkStone import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^about/', views.about),
    url(r'^res/', views.res),
    url(r'^res2/', views.res2),
    url(r'^addres/', views.addres),
    url(r'^res_show/',views.res_show),
    url(r'^article/', views.article),
    url(r'^ask/', views.ask),
    url(r'^video/', views.video),
    url(r'^admin-login', views.admin_login),
    url(r'^login_register/', views.login_register),
    url(r'^email/', views.email),
    url(r'^admin_index/', views.admin_index),
    #url(r'^accounts/', include('users.urls')),
    url(r'^addarticle/', views.addarticle),
    url(r'^article_show/', views.article_show),
    url(r'^AddArticleForm/', views.AddArticleForm),
    url(r'^AddResForm/', views.AddResForm),
    url(r'^login/', views.login),
    url(r'^login_error', views.login_error),
    url(r'^logup/', views.logup),
    url(r'^logup_success/', views.login_register),
    url(r'^login_again/',views.login_again),
    url(r'^usename/', views.usename),
    url(r'^login_success/', views.login_success),
    #url(r'^mongonaut/', include('mongonaut.url')),
    url(r'^logout/', views.logout),
    url(r'^my/',views.my),
    url(r'^token_error/', views.token_error),
    url(r'^activate/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$', views.active_user, name='active_user')


]
