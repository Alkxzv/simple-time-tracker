from .base import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_ROOT = os.environ.get('STATIC_ROOT')
TEMPLATE_DEBUG = False
WSGI_APPLICATION = 'sitt.wsgi.application'
ALLOWED_HOSTS = ['sitt.lkxz.net']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('POSTGRES_PORT_5432_TCP_ADDR'),
        'NAME': 'sittdb',
        'PASSWORD': os.environ.get('POSTGRES_ENV_POSTGRES_PASSWORD'),
        'PORT': os.environ.get('POSTGRES_PORT_5432_TCP_PORT'),
        'USER': 'postgres',
    }
}
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.environ.get('LOG_FILE', '/tmp/sitt-django.log'),
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
