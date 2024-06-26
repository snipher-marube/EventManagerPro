from .base import *
from decouple import config

# Replace the DATABASES section of your settings.py with this
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('PGDATABASE'),
    'USER': config('PGUSER'),
    'PASSWORD': config('PGPASSWORD'),
    'HOST': config('PGHOST'),
    'PORT': config('PGPORT', 5432),
    'OPTIONS': {
      'sslmode': 'require',
    },
  }
}

DEBUG = False