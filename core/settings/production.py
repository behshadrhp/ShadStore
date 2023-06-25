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
