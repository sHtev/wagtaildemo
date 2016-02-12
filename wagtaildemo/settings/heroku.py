import dj_database_url
import os

from .base import *


DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'

DATABASES = {'default': dj_database_url.config(default='postgres://postgres@localhost:5432/wagtaildemo')}

INSTALLED_APPS += ['storages',]
AWS_STORAGE_BUCKET_NAME = 'wagtail-demo'
DEFAULT_FILE_STORAGE = 'storages.backend.s3boto.S3BotoStorage'
MEDIA_URL = ''

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

try:
    from .local import *
except ImportError:
    pass
