from .base import *
from decouple import config
from django.core.management.utils import get_random_secret_key

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default=get_random_secret_key())

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

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
    '.vercel.app',
]

DOMAIN = "http://localhost:8000"
SECURE_SSL_REDIRECT = False

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000"]

