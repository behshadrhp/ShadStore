import os

from .main import *

import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
secret_key = "d&o+*0+i$lcuf=bo8gf^8i=@jevu51j=^37op52!(8nt+c7!ff"
SECRET_KEY = os.environ.setdefault("SECRET_KEY", secret_key)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'shadstore.ir']

# Database
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL')),
}

# SSL & HSTS
SECURE_SSL_REDIRECT = os.env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SECURE_HSTS_SECONDS = os.env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000) # 30 days
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS",default=True)
SECURE_HSTS_PRELOAD = os.env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)

# COOKIE
SESSION_COOKIE_SECURE = os.env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = os.env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)