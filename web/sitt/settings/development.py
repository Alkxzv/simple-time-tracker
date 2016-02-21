from .base import *

SECRET_KEY = 'development'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'sitt',
        'PASSWORD': '',
        'PORT': 5432,
        'USER': 'postgres',
    }
}
INSTALLED_APPS += (
    'debug_toolbar',
)
