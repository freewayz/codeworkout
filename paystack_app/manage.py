#!/usr/bin/env python
import os
import sys

from  utility.utils import  ENV_MODE



if __name__ == "__main__":

    if ENV_MODE == 'dev' or ENV_MODE == 'development':
         os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paystack_app.settings.development")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "paystack_app.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
