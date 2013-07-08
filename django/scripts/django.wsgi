import os, sys
sys.path.append('/opt/bitnami/apps/django/django_projects')
sys.path.append('/opt/bitnami/apps/django/django_projects/Project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Project.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
