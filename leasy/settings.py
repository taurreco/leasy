"""
Django settings for leasy project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))
env_file = BASE_DIR / "leasy/.env"
environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # third party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "corsheaders",
    "drf_spectacular",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "rest_framework",
    "rest_framework.authtoken",
    # local
    "accounts.apps.AccountsConfig",
    "listings.apps.ListingsConfig", # new
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://localhost:8000",
)

CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]


ROOT_URLCONF = "leasy.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "frontend/build/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "leasy.wsgi.application"


# REST Framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSIONS_CLASSES": [
        "rest_framework.permissions.AllowAny",
        # "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# API Schema Documentation
# https://drf-spectacular.readthedocs.io/en/latest/settings.html
SPECTACULAR_SETTINGS = {
    "TITLE": "Leasy",
    "DESCRIPTION": "A website to connect buyers and sellers in the subleasing market",
    "VERSION": "1.0.0",
}


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "leasy",
        "USER": "postgres",
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": "localhost",
        "PORT": 5432,
    }
}

# User authentication
AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "homepage"

## django-allauth settings
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = "email"  # Default: 'username'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1  # Default: 3
ACCOUNT_EMAIL_REQUIRED = True  # Default: False
ACCOUNT_EMAIL_VERIFICATION = "mandatory"  # Default: 'optional'
ACCOUNT_ADAPTER = (
    "accounts.adapter.CustomAccountAdapter"  # for changing confirm email url
)
ACCOUNT_CONFIRM_EMAIL_ON_GET = True  # Default: False
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10  # Default: 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300  # Default 300
ACCOUNT_USERNAME_REQUIRED = False  # Default: True
SITE_ID = 1  # django-allauth requires a default site

## dj-rest-auth settings
# https://dj-rest-auth.readthedocs.io/en/latest/configuration.html

REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "accounts.serializers.CustomRegisterSerializer"
}

REST_AUTH_SERIALIZERS = {
    "LOGIN_SERIALIZER": "accounts.serializers.CustomLoginSerializer"
}

REST_AUTH_REGISTER_PERMISSION_CLASSES = {
    "rest_framework.permissions.AllowAny",
}

# Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = "static/"
STATICFILES_DIRS = [BASE_DIR / "frontend/build/static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
