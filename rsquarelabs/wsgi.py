"""
WSGI config for rsquarelabs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os



import sys

# TODO - Add python packages to the path if using virtualenv
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__)) #adding the parent directory to the python path
WORK_DIRECTORY = os.path.join(CURRENT_DIRECTORY, '..') #adding the project to the python path
sys.path.append(WORK_DIRECTORY)
sys.path.append(os.path.join(WORK_DIRECTORY, '..'))


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rsquarelabs.settings")

application = get_wsgi_application()
