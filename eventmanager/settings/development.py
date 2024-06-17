from .base import *
from decouple import config
from django.core.management.utils import get_random_secret_key

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY = config('SECRET_KEY', default=get_random_secret_key())

DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]

DOMAINS = ['http://localhost:8000', 'http://127.0.0.1:8000']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://127.0.0.1:8000']

