

import os
from django.core.wsgi import get_wsgi_application
from utility.utils import ENV_MODE




"""
    Since we can do more logic in our python file 
"""

if ENV_MODE == 'dev' or ENV_MODE == 'development':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paystack_app.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paystack_app.settings.production")

application = get_wsgi_application()
