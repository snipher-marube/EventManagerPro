from .base import *
from decouple import config
from django.core.management.utils import get_random_secret_key
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY = config('SECRET_KEY', default=get_random_secret_key())

DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

DOMAINS = ['http://localhost:8000', 'http://127.0.0.1:8000']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000']

