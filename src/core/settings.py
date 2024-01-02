from pathlib import Path


# base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# project secret
SECRET_KEY = (
    "django-insecure-ub+-jnd!u&-gu%z^z=&33b-dpdnj62s&2yvd^i3t=ffem_q51k"  # noqa: E501
)

# debug mode
DEBUG = True

# allowed CORS hosts
ALLOWED_HOSTS = []


# installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
]

# middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# path to root url config file
ROOT_URLCONF = "core.urls"

# path to wsgi application
WSGI_APPLICATION = "core.wsgi.application"

# templates setup
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# database setup
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa: E501
    },
]


# english language
LANGUAGE_CODE = "en-us"
# indian timezone
TIME_ZONE = "Asia/Kolkata"
# use internationalization
USE_I18N = True
# use timezone
USE_TZ = True


# path of static files
STATIC_URL = "static/"

# default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
