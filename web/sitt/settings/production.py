from .base import *

SECRET_KEY = os.environ['SITT_SECRET_KEY']
DEBUG = False
TEMPLATE_DEBUG = False
WSGI_APPLICATION = 'sttr.wsgi.application'
