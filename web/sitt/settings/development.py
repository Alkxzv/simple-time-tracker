from .base import *

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sitt.sqlite3',
    }
}
INSTALLED_APPS += (
    'debug_toolbar',
)
