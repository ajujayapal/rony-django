from .base import *
from config.env import env


# DEBUG = env.bool('DJANGO_DEBUG', default=False)

DEBUG = False

# ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
ALLOWED_HOSTS = [
    'ronykoshy.com',
    'www.ronykoshy.com',
    'rony-django-production.up.railway.app',
    'www.rony-django-production.up.railway.app',
    ]

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 1209600 # 2 WEEKS
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Railway settings? (I think)
# CSRF_TRUSTED_ORIGINS = [
#     'https://ronykoshy.com',
#     'https://www.ronykoshy.com',
#     'https://rony-django-production.up.railway.app',
#     'https://www.rony-django-production.up.railway.app',
#     'http://rony-django-production.up.railway.app',
#     'http://www.rony-django-production.up.railway.app',
# ]


# AWS
# from config.settings.file_storage import *

# Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
WHITENOISE_USE_FINDERS = True
WHITENOISE_AUTOREFRESH = DEBUG

# DATABASE

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('PG_DATABASE'),
#         'USER': env('PG_USER'),
#         'PASSWORD': env('PG_PASSWORD'),
#         'HOST': env('PG_HOST'),
#         'PORT': env('PG_PORT'),
#     }
# }

DATABASES = {
    "default": env.db(default="sqlite:///db.sqlite3"),
}

# Appliku Documentation
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    },
}