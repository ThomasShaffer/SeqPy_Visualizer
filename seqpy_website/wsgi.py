"""
WSGI config for seqpy_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

"""
WSGI - Web Server Gateway Interface. Standardized interface for web servers
and web applications to communicate. Portability across different web servers.
Anything that adheres to wsgi can communicate with servers that knew wsgi. 

Important 'environ' dictionary variable which has keys:
REQUEST_METHOD
PATH_INFO
SERVER_PROTOCOL
wsgi.input

application(start_response, environ)
"""


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seqpy_website.settings')

application = get_wsgi_application()
