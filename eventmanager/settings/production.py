from .base import *
from decouple import config
import dj_database_url

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
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
DATABASES['default']['CONN_MAX_AGE'] = 60

DEBUG = False