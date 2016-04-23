__author__ = 'pitaside'


from base import  *



SECRET_KEY = SECRET_KEY


DEV_APPS = [
    'debug_toolbar'
]

INSTALLED_APPS += DEV_APPS

DEV_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

MIDDLEWARE_CLASSES += DEV_MIDDLEWARE

DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'paystack_app',
        'USER' : 'postgres',
        'PASSWORD' : 'postgres_db_password',
        'HOST' : 'localhost',
        'PORT' : 5432
    }
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False






