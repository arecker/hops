from hops.settings.common import *

SECRET_KEY = 'be-hoppy'
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'temp/db.sqlite3'),
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'temp/uploads')
STATIC_ROOT = os.path.join(BASE_DIR, 'temp/static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

AUTH_PASSWORD_VALIDATORS = []

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'temp', 'email')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'temp', 'debug.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG'
        },
    }
}

CURATOR_EMAIL = 'alex@reckerfamily.com'

GOOGLE_ANALYTICS_ID = 'LOL_NOT_A_REAL_KEY'
