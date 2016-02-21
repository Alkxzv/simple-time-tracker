import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INSTALLED_APPS = [
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
]
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'sitt.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            "common.context_processors.common_context",
        ],
    },
}]
WSGI_APPLICATION = 'sitt.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
AUTH_PASSWORD_VALIDATORS = [{
    'NAME':
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
}, {
    'NAME':
    'django.contrib.auth.password_validation.MinimumLengthValidator',
}, {
    'NAME':
    'django.contrib.auth.password_validation.CommonPasswordValidator',
},  {
    'NAME':
    'django.contrib.auth.password_validation.NumericPasswordValidator',
}]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Brussels'
USE_I18N = False
USE_L10N = False
USE_TZ = True
DATETIME_FORMAT = 'Y-m-d D H:i'
DATE_FORMAT = 'Y-m-d'
STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = 'tracker:main'
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
