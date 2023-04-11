from .settings import *
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "football",
        "USER": "root",
        "PASSWORD": "wobuhuiwan",
        "HOST": "lpksir.cn",
        "PORT": "3306",
    }
}