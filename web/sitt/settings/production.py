from .base import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_ROOT = '/sitt/static'
WSGI_APPLICATION = 'sitt.wsgi.application'
ALLOWED_HOSTS = ['.lkxz.net']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'sitt',
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'PORT': 5432,
        'USER': os.environ.get('POSTGRES_USER'),
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/sitt/logs',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
