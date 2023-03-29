from .base import *
from pathlib import Path
import environ
from django.core.management.utils import get_random_secret_key
import cloudinary
import cloudinary_storage

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

CLOUDINARY_STORAGE = {
    'CLOUD_NAME':  env.str('CLOUD_NAME'),
    'API_KEY': env.str('API_KEY'),
    'API_SECRET': env.str("API_SECRET"),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default=get_random_secret_key())  # <-- Updated!

try:
    from .local import *
except ImportError:
    pass
