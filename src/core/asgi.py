import os
from django.core.asgi import get_asgi_application


# specify setting module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# get asgi application
application = get_asgi_application()
