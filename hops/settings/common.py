import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # 3rd Party Apps
    'sorl.thumbnail',
    'pagedown',
    'markdown_deux',
    'compressor',

    # Project Apps
    'content'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'hops.middleware.Timezone'
]

ROOT_URLCONF = 'hops.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom processors
                'hops.processors.settings',
                'hops.processors.advertisement',
                'hops.processors.path',
                'hops.processors.analytics'
            ],
        },
    },
]

WSGI_APPLICATION = 'hops.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/'
STATIC_URL = '/static/'

DOMAIN = 'thehopsmuseum.org'  # no trailing slash or protocol
CURATOR_EMAIL = 'erin@thehopsmuseum.org '
NON_PROFIT_ID = '47-2358924'
WIKI_URL = 'http://wiki.thehopsmuseum.org'
GOOGLE_MAPS_URL = 'https://goo.gl/maps/D26D9jLa5iF2'
FACEBOOK_URL = 'https://www.facebook.com/thehopsmuseum/'
TWITTER_URL = 'https://twitter.com/thehopsmuseum'
INSTAGRAM_URL = 'https://www.instagram.com/thehopsmuseum/'
GITHUB_URL = 'https://github.com/arecker/hops'
GOOGLE_ANALYTICS_ID = 'UA-42540208-11'

VERSION = 'v1.0.4'
