from .base import *
from decouple import config
import dj_database_url

# Replace the DATABASES section of your settings.py with this
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
DATABASES['default']['CONN_MAX_AGE'] = 60

DEBUG = False