from .settings import *
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "happyf_db",
        "USER": "root",
        "PASSWORD": "wobuhuiwan",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}