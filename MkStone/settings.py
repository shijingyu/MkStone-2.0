#coding:utf-8
"""
Django settings for MkStone project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from mongoengine import connect
# #

import time
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bb+u$i3$agyi2br0rx(dsaokh&2h3k&&y^h@#ok7!u&k+^g9)l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
AUTHENTICATION_BACKENDS = ( 'django.contrib.auth.backends.ModelBackend', )
ALLOWED_HOSTS = []
#DOMAIN = 'http://www.shitouboy.com'
DOMAIN = 'http://localhost:8000'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'PythonMkStone',
    #'mongoengine',
    #'mongonaut',
    #'mongo_sessions'

]
#SESSION_ENGINE = 'mongo_sessions.session'

# MONGO_PORT = 27017
# MONGO_HOST = 'localhost'
# MONGO_DB_NAME = 'MkStone'
# MONGO_DB_USER = False
# MONGO_DB_PASSWORD = False
# MONGO_SESSIONS_COLLECTION = 'mongo_sessions'
# MONGO_SESSIONS_TTL = 60 * 60



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MkStone',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

TIME_ZONE = 'Asia/Shanghai'

ROOT_URLCONF = 'MkStone.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MkStone.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
#
# from mongoengine import *
# #
# co('shijingyu')




# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'



USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
# TATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "common_static"),
#     '/path/to/others/static/',  # 用不到的时候可以不写这一行
# )
# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder"
# )

EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'shijy675497282@163.com'
EMAIL_HOST_PASSWORD = '199110127638nice'
EMAIL_PORT = 994   #465，994
EMAIL_USE_SSL = True