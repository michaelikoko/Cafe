from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-yo0fsbquhyh(nb#^lspwvk0yr^+gq%i%@rfwx#+zdr1wwqpyae"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

#import cloudinary
#import cloudinary_storage
#import environ

#env = environ.Env()

#CLOUDINARY_STORAGE = {
#    'CLOUD_NAME':  'dmdm4nogv',
#    'API_KEY': '812873894272894',
#    'API_SECRET': 'FnQ1YngbzUbpgQXqGATKbLXwkJI',
#}

#DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

try:
    from .local import *
except ImportError:
    pass
