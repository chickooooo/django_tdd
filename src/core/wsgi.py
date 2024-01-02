import os
from django.core.wsgi import get_wsgi_application


# specify setting module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# get wsgi application
application = get_wsgi_application()
