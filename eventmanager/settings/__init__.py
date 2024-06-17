import os

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'eventmanager.settings.production':
    from .production import *
else:
    from .development import *
    