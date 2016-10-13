__author__ = 'Soo'
from config.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'easyphoto_dev',
        'USER': 'easyphoto_dev',
        'PASSWORD': 'easyphoto_password',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
