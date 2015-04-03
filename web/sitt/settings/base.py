import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ALLOWED_HOSTS = ['lkxz.net']
INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'common',
    'tracker',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages",
    "common.context_processors.common_context",
)
LOGIN_REDIRECT_URL = 'tracker:main'
STATIC_URL = '/static/'
ROOT_URLCONF = 'sitt.urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Brussels'
USE_I18N = False
USE_L10N = False
USE_TZ = False
DATETIME_FORMAT = 'Y-m-d H:i'
DATE_FORMAT = 'Y-m-d'
COMMON_CONTEXT = {
    'site_name': 'Simple Time Tracker',
    'css_includes': (
        'bower_components/bootstrap/dist/css/bootstrap.min.css',
        'bower_components/nvd3/nv.d3.min.css',
        'custom_bootstrap/css/bootstrap.min.css',
        'css/style.css',
        'tracker/style.css',
    ),
    'js_includes': (
        'bower_components/jquery/dist/jquery.min.js',
        'bower_components/bootstrap/dist/js/bootstrap.min.js',
        'bower_components/d3/d3.min.js',
        'bower_components/nvd3/nv.d3.min.js',
        'tracker/nvd3Charts.js',
    ),
}
GRAPPELLI_ADMIN_TITLE = COMMON_CONTEXT['site_name']
