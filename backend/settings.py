from pathlib import Path
import os
import environ
import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-lb20fhk-*omdr5^!z_ntq((5(*(oy!@jqq5q(ps47o*srt(l*^"

VERSION_NUMBER = "0.1.0"

env = environ.Env(
    DEBUG=(bool, True),
    DATABASE_URL=(str, ""),
    ENVIRONMENT=(str, "DEVELOPMENT"),
    ALLOWED_HOSTS=(str, "127.0.0.1;localhost"),
    ENABLE_SENTRY=(bool, False),
    SENTRY_DSN=(str, ""),
    SECRET_KEY=(str, "demo123"),
    EMAIL_PORT=(int, 587),
    EMAIL_HOST=(str, "smtp.gmail.com"),
    EMAIL_HOST_USER=(str, ""),
    EMAIL_HOST_PASSWORD=(str, ""),
    EMAIL_USE_TLS=(bool, False),
    EMAIL_USE_SSL=(bool, False),
    MEDIA_ROOT=(str, "media_files"),
    STATIC_ROOT=(str, "staticfiles"),
)
environ.Env.read_env()

DEBUG = env("DEBUG")
ENVIRONMENT = env("ENVIRONMENT")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(";")
CORS_ORIGIN_WHITELIST = [f"http://{url}" for url in env("ALLOWED_HOSTS").split(";")]
CORS_ORIGIN_WHITELIST += [f"https://{url}" for url in env("ALLOWED_HOSTS").split(";")]
CORS_ORIGIN_WHITELIST.sort()

# Sentry Configuration

if env("ENABLE_SENTRY"):
    sentry_sdk.init(
        dsn=env("SENTRY_DSN"),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )

# Email Settings

DEFAULT_FROM_EMAIL = "no-reply@pythoncientifico.ar"
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS", False) in ["on", "true"]
EMAIL_USE_SSL = os.environ.get("EMAIL_USE_SSL", False) in ["on", "true"]


INSTALLED_APPS = [
    "polymorphic",
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "sorl.thumbnail",
    "rest_framework",
    "widget_tweaks",
    "crispy_forms",
    "crispy_bootstrap5",
    "import_export",
    "qr_code",
    "conferences",
    "pages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "pages", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"

DATABASES = {}
DATABASES["default"] = dj_database_url.parse(env("DATABASE_URL"), conn_max_age=600)

if ENVIRONMENT == "DEVELOPMENT":
    AUTH_PASSWORD_VALIDATORS = []

else:
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

# Django.contrib.auth settings

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Crispy Forms settings
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# TZ settings
LANGUAGE_CODE = "es"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_L10N = False
USE_TZ = True

# STATIC_ROOT = os.environ.get("STATIC_ROOT", "staticfiles")
STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_ROOT = os.environ.get("MEDIA_ROOT", "media")
MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
