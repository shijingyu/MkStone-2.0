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
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^about/', views.about),
    url(r'^res/', views.res),
    url(r'^article/', views.article),
    url(r'^ask/', views.ask),
    url(r'^video/', views.video),
    url(r'^login_register/', views.login_register),
    url(r'^email/', views.email),
    url(r'^admin_index/', views.admin_index),
    url(r'^accounts/', include('users.urls'))
]
