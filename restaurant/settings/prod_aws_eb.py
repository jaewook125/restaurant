
from .common import *
import os

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'USER': DB_USER_NAME,
        'PASSWORD': DB_PASSWORD,
        'NAME': DB_NAME,
        'PORT': '',
    },
}
