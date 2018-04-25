# import our default settings
from settings_common import *

import ast

from dj_database_url import parse as db_parse
from decouple import config
from decouple import Csv
from redis.sentinel import Sentinel

# Nyaruka settings.
from .settings_common import *  # noqa


REDIS_HOST = config('REDIS_HOST', default='redis')
BROKER_HOST = REDIS_HOST
BROKER_BACKEND = 'redis'
BROKER_PORT = config('REDIS_PORT', default=6379, cast=int)
BROKER_VHOST = '1'
BROKER_URL = '%s://%s:%s/%s' % (BROKER_BACKEND, BROKER_HOST, BROKER_PORT, BROKER_VHOST)
CELERY_RESULT_BACKEND = BROKER_URL
CACHES['default']['LOCATION'] = BROKER_URL

GDAL_LIBRARY_PATH = config('GDAL_LIBRARY_PATH', default='/usr/lib/libgdal.so.20')
GEOS_LIBRARY_PATH = config('GEOS_LIBRARY_PATH', default='/usr/lib/libgeos_c.so.1')

DEBUG_TOOLBAR = config('DEBUG_TOOLBAR', default=False, cast=bool)
DEBUG = config('DEBUG', default=False, cast=bool)

# Available languages for translation
LANGUAGES = (('en', "English"), ('fr', "French"), ('es', "Spanish"), ('ar', "Arabic"),
             ('uk', "Ukrainian"), ('pt-br', 'Portuguese'), ('th', "Thai"), ('ro', "Romanian"))

API_BOUNDARY_CACHE_TIME = 30
API_GROUP_CACHE_TIME = 30
API_RESULT_CACHE_TIME = 30
API_CONTACT_RESULT_CACHE_TIME = 30
API_CONTACTS_CACHE_TIME = 30
API_FLOWS_CACHE_TIME = 30

INSTALLED_APPS = INSTALLED_APPS + ('gunicorn', 'raven.contrib.django.raven_compat',)

EMPTY_SUBDOMAIN_HOST = config('EMPTY_SUBDOMAIN_HOST', default='http://ureport.in')
HOSTNAME = config('HOSTNAME', default='localhost')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())
SESSION_COOKIE_DOMAIN = config('SESSION_COOKIE_DOMAIN', default='ureport.in')
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', False, cast=bool)

ANONYMOUS_USER_NAME = config('ANONYMOUS_USER_NAME', default='AnonymousUser')

# these guys will get email from sentry
ADMINS = config('ADMINS', default='((),)', cast=ast.literal_eval)

TIME_ZONE = config('TIME_ZONE', default='America/Sao_Paulo')
USER_TIME_ZONE = config('USER_TIME_ZONE', default='America/Sao_Paulo')

# set the mail settings, we send through gmail

EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_ALIAS = config('EMAIL_ALIAS', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default=EMAIL_ALIAS)

ANONYMOUS_USER_ID = -1

MANAGERS = ADMINS

# Set your DSN value
RAVEN_CONFIG = {'dsn': config('RAVEN_DSN', default='')}

# we store files on S3 on prod boxes
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', default='')
AWS_S3_SECURE_URLS = config('AWS_S3_SECURE_URLS', default=True, cast=bool)
DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE', default='storages.backends.s3boto3.S3Boto3Storage')

# these two settings will cause our aws files to never expire
# see http://developer.yahoo.com/performance/rules.html#expires
AWS_QUERYSTRING_AUTH = config('AWS_QUERYSTRING_AUTH', default=False, cast=bool)
AWS_HEADERS = config('AWS_HEADERS',
                     default="{'Expires': 'Wed, 1 Jan 2020 20:00:00 GMT', 'Cache-Control': 'max-age=86400'}",
                     cast=ast.literal_eval)

COMPRESS_ENABLED = config('COMPRESS_ENABLED', default=True, cast=bool)
# static dir is different for prod
STATIC_URL = config('STATIC_URL', default='/sitestatic/')
COMPRESS_URL = config('COMPRESS_URL', default=STATIC_URL)
COMPRESS_CSS_HASHING_METHOD = config('COMPRESS_CSS_HASHING_METHOD', default='content')
COMPRESS_OFFLINE = config('COMPRESS_OFFLINE', default=False, cast=bool)
COMPRESS_OFFLINE_CONTEXT = config('COMPRESS_OFFLINE_CONTEXT',
                                  default="""{'STATIC_URL': '%s',
                                               'base_template': 'frame.html',
                                               'debug': False,
                                               'testing': False}""" % STATIC_URL,
                                  cast=ast.literal_eval)

# our media is all on S3
MEDIA_URL = config('MEDIA_URL', default='http://ureport.ilhasoft.mobi/media/')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SITE_API_HOST = config('SITE_API_HOST', default='https://rapidpro.ilhasoft.mobi')
API_ENDPOINT = config('API_ENDPOINT', default='https://rapidpro.ilhasoft.mobi')

# reuse our connections for up to 60 seconds
DATABASES['default'] = config('DATABASE_URL',
                              default='postgres://temba:temba@database/ureport',
                              cast=db_parse)
DATABASES['default']['CONN_MAX_AGE'] = 60

CELERY_ALWAYS_EAGER = config('CELERY_ALWAYS_EAGER', default=False, cast=bool)
CELERY_EAGER_PROPAGATES_EXCEPTIONS = config('CELERY_EAGER_PROPAGATES_EXCEPTIONS', default=True, cast=bool)