"""
WSGI config for restoran project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information.txt on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restoran.settings')

application = get_wsgi_application()
