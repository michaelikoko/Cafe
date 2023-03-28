from .base import *
from pathlib import Path
import environ
from django.core.management.utils import get_random_secret_key


env = environ.Env( 
    DEBUG=(bool, False),
)

#DEBUG = False

ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

#CSRF_TRUSTED_ORIGINS = ['*']

#SECURE_SSL_REDIRECT = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default=get_random_secret_key())  # <-- Updated!

try:
    from .local import *
except ImportError:
    pass
