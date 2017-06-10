import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^=xgnpd%4wl+jh(j2+&8ms_eo*1qy7s7y7lib#9)meq)fppf_p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TODO: Set this to localhost, and the ip / dns name of server
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django AllAuth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',

    # Django Admin Tools
    #'admin_tools',
    #'admin_tools.theming',
    #'admin_tools.menu',
    #'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',

    # django-crispy-forms
    'crispy_forms',

    # site apps
    'stockpile_tv',
    'users',
    'subscriptions',
    'subreddit_videos',

    # Test suite
    'django_nose',
]

SITE_ID = 1

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_DIR = os.path.dirname(SETTINGS_DIR)

##########################################################################
#
#  Authentication settings
#
##########################################################################

# When a user successfully logs in, redirect here by default
LOGIN_REDIRECT_URL = '/'

# Require that users who are signing up provide an email address
ACCOUNT_EMAIL_REQUIRED = False

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Django Guardian settings
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'allauth.account.auth_backends.AuthenticationBackend',
)
ANONYMOUS_USER_ID = -1

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda u: "/profile/%s/" % u.username,
}

##########################################################################
#
# Crispy settings
#
##########################################################################

CRISPY_TEMPLATE_PACK = 'bootstrap3'

##########################################################################
#
# Testing settings
#
##########################################################################

# Sets the testrunner to Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

##########################################################################
#
# Location settings
#
##########################################################################

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = True

##########################################################################
#
# Travis Settings
#
##########################################################################
if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'travisci',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stockpile_tv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.media",
                'django.core.context_processors.i18n',

            ],
            'loaders': [
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.filesystem.Loader',
            ]
        },
    },
]

WSGI_APPLICATION = 'stockpile_tv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
