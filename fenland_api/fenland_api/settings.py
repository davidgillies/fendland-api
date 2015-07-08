"""
Django settings for fenland_api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$(qgib-)0yl&zu7#6+1++b(!7w$jo2sgiu=2j!0#nzxynrjrv0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.admindocs',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'debug_toolbar',
    'rest_framework',
    'django_extensions',
    'questionnaire',
    'api_renderer',
    'html_renderer',
    'import_export',
    'adminplus',
    'explorer',
)

ADMIN_TOOLS_INDEX_DASHBOARD = 'api_renderer.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'api_renderer.dashboard.CustomAppIndexDashboard'
ADMIN_TOOLS_MENU = 'api_renderer.menu.CustomMenu'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'html_renderer.middleware.BeautifulMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'fenland_api.urls'

WSGI_APPLICATION = 'fenland_api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'db2': {
        'ENGINE': 'django_mysql_fix.backends.mysql',
        'NAME': 'mydb',
        'USER': 'david',
        'PASSWORD': 'david',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'db3': {
        'ENGINE': 'django_mysql_fix.backends.mysql',
        'NAME': 'mrc_epid_fenland',
        'USER': 'david',
        'PASSWORD': 'david',
        'HOST': 'localhost',
        'PORT': '3306',
    },
}

EXPLORER_CONNECTION_NAME = 'db2'

DATABASE_ROUTERS = ['api_renderer.routers.PlayRouter', 'questionnaire.routers.PlayRouter', ]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

#TEMPLATE_LOADERS = (
#    ('django.template.loaders.cached.Loader', (
#        'django.template.loaders.filesystem.Loader',
#        'django.template.loaders.app_directories.Loader',
#    )),
#)

STATIC_ROOT = 'U:/Data/fenland_api/fendland-api/static'

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE = 1

SITE_ID = 2

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
