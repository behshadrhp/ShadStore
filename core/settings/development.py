from .main import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+rmlr_#2w2^#thf5y^fs_b&ns_jbc&igt5b&etsw9bs7$%d^m$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
