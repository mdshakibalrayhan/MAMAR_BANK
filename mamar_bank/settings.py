"""
Django settings for mamar_bank project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#import environ

# Initialize environment variables
import environ

env = environ.Env()
environ.Env.read_env()  # Loads the .env file

# Secret key
SECRET_KEY = env("SECRET_KEY", default="fallback-secret-key")
'''
# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME", default="default_db_name"),
        'USER': env("DB_USER", default="default_user"),
        'PASSWORD': env("DB_PASSWORD", default="default_password"),
        'HOST': env("DB_HOST", default="localhost"),
        'PORT': env("DB_PORT", default="5432"),
    }
}'''
# Database documentation https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://mamar_bank_z2gg_user:v01HNqoKWQaDlyXcHRMmIPznaqQyxIuy@dpg-cu5vpkjtq21c7383ve30-a.oregon-postgres.render.com/mamar_bank_z2gg',
    )
}
SECRET_KEY = 'django-insecure-mes$n&n65xj%l60*%l1bo#g$c0s7j9c$jck6nuuq-=b@zbr_5u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'accounts',
    'core',
    'transactions',
    'crispy_forms',
    'crispy_bootstrap5', 
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" 
CRISPY_TEMPLATE_PACK = "bootstrap5"          


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mamar_bank.urls'

TEMPLATES = [
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
]

WSGI_APPLICATION = 'mamar_bank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}'''
import environ
env = environ.Env()
environ.Env.read_env()

# Your secret key
#SECRET_KEY = env("SECRET_KEY")
#SECRET_KEY = 'django-insecure-mes$n&n65xj%l60*%l1bo#g$c0s7j9c$jck6nuuq-=b@zbr_5u'#env("SECRET_KEY")
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Loads the .env file

# Secret key
SECRET_KEY = env("SECRET_KEY", default="fallback-secret-key")

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME", default="default_db_name"),
        'USER': env("DB_USER", default="default_user"),
        'PASSWORD': env("DB_PASSWORD", default="default_password"),
        'HOST': env("DB_HOST", default="localhost"),
        'PORT': env("DB_PORT", default="5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL_HOST_USER") #sender's email-id
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")#password associated with above email-id (not the regular password)
