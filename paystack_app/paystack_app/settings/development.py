__author__ = 'pitaside'

from base import *

SECRET_KEY = SECRET_KEY

# DEV_APPS = [
#     'debug_toolbar'
# ]
#
# INSTALLED_APPS += DEV_APPS

DEV_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

# MIDDLEWARE_CLASSES += DEV_MIDDLEWARE

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False
