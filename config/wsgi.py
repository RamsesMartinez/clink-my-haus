"""
WSGI config for clinkmyhaus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import environ

from django.core.wsgi import get_wsgi_application

env = environ.Env()

ROOT_DIR = environ.Path(__file__) - 2

env.read_env('.env')

env.str('DJANGO_SETTINGS_MODULE', 'config.settings.local')

application = get_wsgi_application()
