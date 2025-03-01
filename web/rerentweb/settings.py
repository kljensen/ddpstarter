"""
Django settings for rerentweb project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if 'DEVELOPMENT' in os.environ:
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
else:
    DEBUG = False
    ALLOWED_HOSTS = ['.herokuapp.com']

# Allow all host headers for Heroku deploy


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_datepicker_plus',
    'awaydays'
]

MIDDLEWARE = [
    # The first few things are defaults
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add whitenoise for static asset handling.
    # See https://devcenter.heroku.com/articles/django-assets
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
# Use gzip for whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cache')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

ROOT_URLCONF = 'rerentweb.urls'

# See https://docs.djangoproject.com/en/2.2/topics/templates/
TEMPLATES = [
    # The following block is default
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    # And we add in jinja2 support
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/jinja2'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'rerentweb.jinja2.environment',
        },
    },
]

WSGI_APPLICATION = 'rerentweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {}
if 'DATABASE_URL' in os.environ:
    # Use DATABASE_URL, which would be provided by Heroku. This is
    # likely to be the case when we're in production.
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
else:
    # Use the POSTGRES_* environment variables. This is likely to
    # be the case when we're in development.
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'HOST': 'db',
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'PORT': os.environ['POSTGRES_PORT'],
    }

# Set a custom user model. See
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
AUTH_USER_MODEL = 'awaydays.User'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BOOTSTRAP4 = {
    'include_jquery': True,
}
